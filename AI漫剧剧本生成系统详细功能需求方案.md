# AI漫剧剧本生成系统详细功能需求方案

## 一、系统总体功能

### 1.1 核心功能
- 剧本自动生成（基于剧情大纲）
- 文档管理（人物、场景、剧情大纲、设定）
- 剧本编辑与管理
- 一致性验证
- 批量生成与进度跟踪

### 1.2 用户角色
- **管理员**: 所有权限
- **编辑者**: 文档编辑、剧本生成、剧本编辑
- **查看者**: 仅查看权限

## 二、后端API详细功能

### 2.1 剧本生成API

#### 2.1.1 单集生成
- **接口**: `POST /api/scripts/generate`
- **请求参数**:
  ```json
  {
    "episode": 1,
    "creativity_level": 0.3,
    "enable_validation": true
  }
  ```
- **响应**:
  ```json
  {
    "code": 200,
    "message": "生成成功",
    "data": {
      "episode": 1,
      "script_id": "script_001",
      "status": "completed",
      "content": "剧本内容...",
      "word_count": 1200,
      "validation_result": {
        "is_valid": true,
        "issues": []
      }
    }
  }
  ```
- **功能**:
  - 根据集数生成剧本
  - 支持创造性级别调整（0-1）
  - 自动进行一致性验证
  - 返回生成状态和结果

#### 2.1.2 批量生成
- **接口**: `POST /api/scripts/generate-batch`
- **请求参数**:
  ```json
  {
    "start_episode": 1,
    "end_episode": 10,
    "creativity_level": 0.3,
    "enable_validation": true
  }
  ```
- **响应**:
  ```json
  {
    "code": 200,
    "message": "批量生成任务已创建",
    "data": {
      "batch_id": "batch_001",
      "total_episodes": 10,
      "status": "processing",
      "progress": 0
    }
  }
  ```
- **功能**:
  - 批量生成多集剧本
  - 创建异步任务
  - 返回任务ID用于进度查询

#### 2.1.3 生成进度查询
- **接口**: `GET /api/scripts/progress/{batch_id}`
- **响应**:
  ```json
  {
    "code": 200,
    "data": {
      "batch_id": "batch_001",
      "total_episodes": 10,
      "completed_episodes": 5,
      "progress": 50,
      "current_episode": 6,
      "status": "processing",
      "episodes": [
        {
          "episode": 1,
          "status": "completed",
          "word_count": 1200
        },
        {
          "episode": 2,
          "status": "completed",
          "word_count": 1150
        },
        {
          "episode": 3,
          "status": "processing",
          "word_count": 0
        }
      ]
    }
  }
  ```
- **功能**:
  - 查询批量生成进度
  - 显示每集生成状态
  - 实时更新进度

#### 2.1.4 WebSocket实时推送
- **接口**: `WS /ws/scripts/progress/{batch_id}`
- **消息格式**:
  ```json
  {
    "type": "progress",
    "data": {
      "batch_id": "batch_001",
      "current_episode": 3,
      "progress": 30,
      "status": "processing"
    }
  }
  ```
- **功能**:
  - 实时推送生成进度
  - 支持多客户端连接
  - 自动断线重连

### 2.2 文档管理API

#### 2.2.1 人物管理
- **获取人物列表**: `GET /api/characters`
  - 支持分页、搜索、筛选
  - 返回人物基本信息
  
- **获取人物详情**: `GET /api/characters/{name}`
  - 返回完整人物信息
  - 包含各阶段状态
  
- **创建人物**: `POST /api/characters`
  ```json
  {
    "name": "张三",
    "identity": "镇北王世子",
    "stages": {
      "前期": {
        "appearance": "外貌描写",
        "identity": "身份描述"
      }
    }
  }
  ```
  
- **更新人物**: `PUT /api/characters/{name}`
- **删除人物**: `DELETE /api/characters/{name}`
- **批量导入人物**: `POST /api/characters/import`
  - 支持Excel、CSV、JSON格式

#### 2.2.2 场景管理
- **获取场景列表**: `GET /api/scenes`
- **获取场景详情**: `GET /api/scenes/{name}`
- **创建场景**: `POST /api/scenes`
  ```json
  {
    "name": "镇北王府·世子寝殿",
    "description": "场景描述",
    "time": "日/夜",
    "type": "内/外"
  }
  ```
- **更新场景**: `PUT /api/scenes/{name}`
- **删除场景**: `DELETE /api/scenes/{name}`

#### 2.2.3 剧情大纲管理
- **获取大纲列表**: `GET /api/outlines`
  - 支持按集数范围筛选
  - 支持按剧情阶段筛选
  
- **获取大纲详情**: `GET /api/outlines/{episode}`
  ```json
  {
    "episode": 1,
    "title": "第1集：血色生辰，画道觉醒",
    "main_progress": "主线推进描述",
    "event_logic": {
      "cause": "起因",
      "process": "经过",
      "result": "结果"
    },
    "hook": "悬念/钩子",
    "climax": "爽点/高潮",
    "highlights": ["亮点1", "亮点2"],
    "conflicts": ["冲突1", "冲突2"]
  }
  ```
  
- **创建大纲**: `POST /api/outlines`
- **更新大纲**: `PUT /api/outlines/{episode}`
- **删除大纲**: `DELETE /api/outlines/{episode}`
- **批量导入大纲**: `POST /api/outlines/import`

#### 2.2.4 设定管理
- **获取设定列表**: `GET /api/settings`
- **获取设定详情**: `GET /api/settings/{key}`
- **创建设定**: `POST /api/settings`
- **更新设定**: `PUT /api/settings/{key}`
- **删除设定**: `DELETE /api/settings/{key}`

### 2.3 剧本管理API

#### 2.3.1 剧本列表
- **接口**: `GET /api/scripts`
- **请求参数**:
  - `page`: 页码
  - `page_size`: 每页数量
  - `episode`: 集数筛选
  - `status`: 状态筛选（completed/processing/failed）
  
- **响应**:
  ```json
  {
    "code": 200,
    "data": {
      "total": 70,
      "page": 1,
      "page_size": 10,
      "items": [
        {
          "script_id": "script_001",
          "episode": 1,
          "title": "第1集：血色生辰，画道觉醒",
          "status": "completed",
          "word_count": 1200,
          "created_at": "2024-01-01 10:00:00",
          "updated_at": "2024-01-01 10:00:00"
        }
      ]
    }
  }
  ```

#### 2.3.2 剧本详情
- **接口**: `GET /api/scripts/{episode}`
- **响应**:
  ```json
  {
    "code": 200,
    "data": {
      "script_id": "script_001",
      "episode": 1,
      "title": "第1集：血色生辰，画道觉醒",
      "content": "完整剧本内容...",
      "word_count": 1200,
      "characters": ["陆念离", "陆长乐", "六剑奴"],
      "scenes": ["镇北王府·世子寝殿", "长安·醉仙楼"],
      "status": "completed",
      "validation_result": {
        "is_valid": true,
        "issues": []
      },
      "created_at": "2024-01-01 10:00:00",
      "updated_at": "2024-01-01 10:00:00"
    }
  }
  ```

#### 2.3.3 剧本编辑
- **接口**: `PUT /api/scripts/{episode}`
- **请求参数**:
  ```json
  {
    "content": "修改后的剧本内容"
  }
  ```
- **功能**:
  - 更新剧本内容
  - 自动重新验证
  - 保存历史版本

#### 2.3.4 剧本导出
- **接口**: `GET /api/scripts/{episode}/export`
- **请求参数**:
  - `format`: 导出格式（markdown）
  
- **功能**:
  - 支持Markdown导出
  - 批量导出

#### 2.3.5 剧本历史版本
- **接口**: `GET /api/scripts/{episode}/history`
- **功能**:
  - 查看历史版本
  - 恢复历史版本
  - 版本对比

### 2.4 验证API

#### 2.4.1 一致性验证
- **接口**: `POST /api/validation/consistency`
- **请求参数**:
  ```json
  {
    "episode": 1,
    "content": "剧本内容"
  }
  ```
- **响应**:
  ```json
  {
    "code": 200,
    "data": {
      "is_valid": true,
      "issues": [],
      "warnings": [],
      "details": {
        "character_consistency": {
          "is_valid": true,
          "issues": []
        },
        "ability_consistency": {
          "is_valid": true,
          "issues": []
        },
        "force_consistency": {
          "is_valid": true,
          "issues": []
        }
      }
    }
  }
  ```

#### 2.4.2 格式验证
- **接口**: `POST /api/validation/format`
- **功能**:
  - 检查剧本格式
  - 检查描写长度
  - 检查连续△数量
  - 检查禁止模式

#### 2.4.3 规则验证
- **接口**: `POST /api/validation/rules`
- **功能**:
  - 检查白描规则
  - 检查人物介绍规则
  - 检查场景描写规则

#### 2.4.4 批量验证
- **接口**: `POST /api/validation/batch`
- **功能**:
  - 批量验证多集剧本
  - 生成验证报告
  - 导出验证报告

### 2.5 系统管理API

#### 2.5.1 配置管理
- **获取配置**: `GET /api/config`
- **更新配置**: `PUT /api/config`
- **重置配置**: `POST /api/config/reset`

#### 2.5.2 状态查询
- **系统状态**: `GET /api/system/status`
  ```json
  {
    "code": 200,
    "data": {
      "status": "healthy",
      "uptime": 86400,
      "memory_usage": 512,
      "cpu_usage": 30,
      "disk_usage": 60,
      "active_tasks": 2
    }
  }
  ```
- **任务状态**: `GET /api/system/tasks`

#### 2.5.3 日志管理
- **获取日志**: `GET /api/system/logs`
  - 支持分页
  - 支持按级别筛选
  - 支持按时间筛选
  
- **导出日志**: `GET /api/system/logs/export`

#### 2.5.4 用户管理
- **用户列表**: `GET /api/users`
- **创建用户**: `POST /api/users`
- **更新用户**: `PUT /api/users/{id}`
- **删除用户**: `DELETE /api/users/{id}`
- **修改密码**: `POST /api/users/{id}/password`

## 三、前端详细功能

### 3.1 首页

#### 3.1.1 项目概览
- 显示项目统计信息
  - 总集数
  - 已生成集数
  - 生成中集数
  - 验证通过率
  
- 显示最近生成记录
  - 集数
  - 生成时间
  - 状态
  - 字数

- 显示系统状态
  - 服务状态
  - CPU使用率
  - 内存使用率
  - 磁盘使用率

#### 3.1.2 快速操作
- 快速生成单集剧本
- 快速验证剧本
- 快速导出剧本
- 快速查看文档

### 3.2 剧本生成页

#### 3.2.1 生成配置
- **集数选择**
  - 单选：选择单集
  - 范围选择：选择集数范围
  - 全选：选择所有集数
  
- **参数配置**
  - 创造性级别滑块（0-1）
  - 是否启用验证（开关）
  - 是否自动保存（开关）
  
- **生成按钮**
  - 点击开始生成
  - 显示生成状态

#### 3.2.2 实时进度
- **进度条**
  - 显示总体进度
  - 显示当前集数
  - 显示剩余时间估算
  
- **进度列表**
  - 显示每集生成状态
  - 显示每集字数
  - 显示每集验证结果
  
- **实时日志**
  - 显示生成日志
  - 显示错误信息
  - 支持滚动查看

#### 3.2.3 生成结果
- **结果预览**
  - 显示生成的剧本内容
  - 支持滚动查看
  - 支持高亮显示
  
- **结果操作**
  - 保存剧本
  - 编辑剧本
  - 导出剧本
  - 重新生成

### 3.3 文档管理页

#### 3.3.1 人物管理
- **人物列表**
  - 表格展示
  - 支持搜索
  - 支持排序
  - 支持分页
  
- **人物详情**
  - 基本信息
  - 各阶段状态
  - 外貌描写
  - 身份描述
  
- **人物编辑**
  - 表单编辑
  - 实时验证
  - 自动保存
  
- **人物导入**
  - 支持Excel导入
  - 支持CSV导入
  - 支持JSON导入
  - 批量导入

#### 3.3.2 场景管理
- **场景列表**
  - 表格展示
  - 支持搜索
  - 支持筛选
  
- **场景编辑**
  - 场景名称
  - 场景描述
  - 时间类型
  - 内外类型

#### 3.3.3 剧情大纲管理
- **大纲列表**
  - 按集数展示
  - 显示标题
  - 显示状态
  
- **大纲编辑**
  - 标题编辑
  - 主线推进编辑
  - 事件逻辑编辑（起因、经过、结果）
  - 悬念/钩子编辑
  - 爽点/高潮编辑
  - 亮点编辑
  - 冲突编辑
  
- **大纲导入**
  - 支持Markdown导入
  - 支持Excel导入
  - 批量导入

#### 3.3.4 设定管理
- **设定列表**
  - 键值对展示
  - 支持搜索
  
- **设定编辑**
  - 键编辑
  - 值编辑
  - 类型选择

### 3.4 剧本管理页

#### 3.4.1 剧本列表
- **列表展示**
  - 表格展示
  - 显示集数
  - 显示标题
  - 显示状态
  - 显示字数
  - 显示更新时间
  
- **筛选与搜索**
  - 按集数筛选
  - 按状态筛选
  - 关键词搜索
  
- **批量操作**
  - 批量导出
  - 批量验证
  - 批量删除

#### 3.4.2 剧本编辑器
- **编辑功能**
  - Markdown编辑
  - 语法高亮
  - 实时预览
  - 自动保存
  
- **辅助功能**
  - 字数统计
  - 格式检查
  - 快捷键支持
  - 撤销重做
  
- **版本管理**
  - 查看历史版本
  - 恢复历史版本
  - 版本对比

#### 3.4.3 剧本导出
- **导出格式选择**
  - Markdown格式导出
  
- **导出选项**
  - 是否包含验证报告
  - 是否包含元数据
  - 是否压缩

### 3.5 验证工具页

#### 3.5.1 一致性验证
- **验证配置**
  - 选择验证类型
  - 选择验证范围
  - 配置验证参数
  
- **验证执行**
  - 点击开始验证
  - 显示验证进度
  - 显示验证结果
  
- **验证报告**
  - 总体结果
  - 详细问题列表
  - 问题定位
  - 修复建议

#### 3.5.2 格式验证
- **格式检查**
  - 描写长度检查
  - 连续△数量检查
  - 禁止模式检查
  
- **问题列表**
  - 显示所有格式问题
  - 显示问题位置
  - 显示修复建议

#### 3.5.3 规则验证
- **规则检查**
  - 白描规则检查
  - 人物介绍规则检查
  - 场景描写规则检查
  
- **规则详情**
  - 显示规则说明
  - 显示违反情况
  - 显示修复建议

## 四、高可用性功能

### 4.1 健康检查
- **服务健康检查**
  - 定期检查服务状态
  - 自动重启失败服务
  - 发送告警通知
  
- **数据库健康检查**
  - 检查数据库连接
  - 检查数据库性能
  - 自动优化数据库

### 4.2 错误处理
- **全局异常捕获**
  - 捕获所有异常
  - 记录详细日志
  - 返回友好提示
  
- **错误码体系**
  - 标准化错误码
  - 错误码文档
  - 错误码查询

### 4.3 数据备份
- **自动备份**
  - 每日自动备份
  - 备份文件管理
  - 备份文件清理
  
- **手动备份**
  - 一键备份
  - 备份下载
  - 备份恢复

### 4.4 性能监控
- **实时监控**
  - CPU监控
  - 内存监控
  - 磁盘监控
  - 网络监控
  
- **性能告警**
  - 阈值配置
  - 告警通知
  - 告警历史

## 五、测试功能

### 5.1 单元测试
- 后端API测试
- 前端组件测试
- 测试覆盖率报告

### 5.2 集成测试
- 前后端联调测试
- API接口测试
- 数据库操作测试

### 5.3 性能测试
- 并发压力测试
- 响应时间测试
- 内存泄漏测试

### 5.4 稳定性测试
- 长时间运行测试
- 异常恢复测试
- 边界条件测试

## 六、实施步骤

### 阶段一：后端开发（3-4天）
1. 搭建FastAPI项目框架
2. 迁移现有核心逻辑到API服务
3. 实现RESTful API接口
4. 实现WebSocket实时通信
5. 添加错误处理和日志
6. 编写单元测试

### 阶段二：前端开发（3-4天）
1. 搭建Vue 3项目框架
2. 实现剧本生成界面
3. 实现文档管理界面
4. 实现剧本管理界面
5. 实现验证工具界面
6. 编写组件测试

### 阶段三：集成测试（1-2天）
1. 前后端联调
2. 功能测试
3. 性能测试
4. Bug修复

### 阶段四：部署配置（1-2天）
1. Docker容器化
2. 配置Nginx
3. 配置Redis
4. 配置监控
5. 配置备份策略

### 阶段五：验收测试（1天）
1. 完整功能测试
2. 稳定性测试
3. 性能验证
4. 文档完善

## 七、质量保证

### 7.1 代码质量
- 代码规范：PEP 8（Python）、ESLint（TypeScript）
- 代码审查：关键代码必须审查
- 文档完善：API文档、用户手册

### 7.2 功能质量
- 现有功能完全保留
- 新功能完整可用
- 用户体验友好

### 7.3 性能质量
- 响应时间：<2s（正常情况）
- 并发支持：100+用户同时使用
- 系统可用性：>99.9%

## 八、风险控制

### 8.1 技术风险
- 新技术学习成本
- 系统复杂度增加
- 性能瓶颈

### 8.2 应对措施
- 技术预研和原型验证
- 分阶段实施，逐步迭代
- 性能测试和优化

## 九、交付物

1. 完整的后端API服务
2. 完整的前端Web应用
3. Docker部署配置
4. 完整的测试报告
5. API文档和用户手册
6. 部署和运维文档

## 十、时间估算

- 总计：8-12天
- 后端开发：3-4天
- 前端开发：3-4天
- 集成测试：1-2天
- 部署配置：1-2天
- 验收测试：1天
