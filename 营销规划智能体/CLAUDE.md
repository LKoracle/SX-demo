# 营销规划智能体 · 项目说明

## 项目背景

本项目是平安人寿内勤系统**平安DO**上的一个 AI 智能体，面向寿险**营销管理人员**（内勤/机构经理层），帮助其完成从目标下发、路径规划、活动推荐到激励方案制定的全流程营销规划工作。智能体的统一入口为平安DO首页的"AskBob"对话框。

## 产品定位

- **产品名称**：营销规划智能体
- **宿主平台**：平安DO（平安人寿内勤智能工作台，Web端）
- **交互方式**：对话式 AI（Chat-based），用户通过自然语言与智能体交互
- **入口位置**：平安DO 首页右侧栏下半部分的 AskBob 卡片，含推荐问题区、输入区、快捷功能区
- **对话页面**：点击入口后跳转至"万能营销助手对话页面"，顶部有"退出对话"按钮可返回首页
- **Agent框架**：OpenClaw（智能体编排平台，平安内部）
- **工具层**：MCP 工具（原子化工具，供 Agent 调用）

## 核心功能模块（优先级）

| 模块 | 优先级 | 核心能力 |
|------|--------|---------|
| 规划达成路径 | P0 | 产品达成路径、客户达成路径、队伍达成路径 
| 目标计划拆解 | P1 | 拆解月度目标、拆解下级目标
| 推荐场景活动 | P1 | 推荐活动频次、匹配活动方案


## 技术架构（四层）

```
交互层
  └─ 平安DO · 营销规划智能体（统一对话入口）
          ↓
Agent 应用层（= OpenClaw 实例）
  └─ 目标计划拆解 / 规划达成路径 / 推荐场景活动 
          ↓
原子化工具层（= MCP 工具）
  └─ 各功能域对应的原子工具（查询/计算/生成/校验/推送）
          ↓
数据层
  └─ 经营指标库 / 客户资源库 / 代理人信息库 / 产品知识库 / 活动方案库 
```

**辅助系统：**
- **智能体平台**：智能体编排、工作流编排、技能与插件管理、记忆管理
- **事件驱动引擎**：经营周期驱动 / 目标下发驱动 / 数据更新驱动

## 目标用户

- **主要用户**：寿险机构经理、营业部主任等营销管理人员（内勤侧）
- **使用场景**：根据业务季，通过对话快速生成目标拆分、路径方案、活动推荐

## 关键文件索引

| 文件 | 说明 |
|------|------|
| `产品功能架构图/营销规划智能体_功能架构图.html/.png` | 完整四层架构图，含各模块功能与技术标注 |
| `PRD/首页AskBob入口_PRD.docx` | 平安DO首页增加营销规划智能体入口的需求文档 |
| `原型图/平安DO_C方案_首页增加入口v0.5.html` | 平安DO首页及智能体交互界面原型（v0.5） |

## 术语表

| 术语 | 含义 |
|------|------|
| 平安DO | 平安人寿内勤智能工作台（桌面Web应用） |
| AskBob | 平安DO首页正上方的AI 对话入口卡片，含推荐问题/输入框俩部分 |
| 万能营销助手 | 点击 AskBob 后跳转的对话页面，即营销规划智能体的完整对话界面 |
| OpenClaw | 平安内部智能体编排平台（本项目 Agent 运行时） |
| MCP 工具 | 原子化工具层，供 Agent 调用的标准化工具 |
| 目标拆分 | 将总部下发的业务季推动目标拆解到月度，并拆解到下辖各营业单位
| 规划达成路径 | 从产品、客户、队伍三条线整合生成可执行经营计划 |
| 寿钻人力 | 达到钻石及以上等级的人力，包含双金钻、金钻、银钻、钻石四个等级，不含活动非钻和非活动人力 |
| 客温/客价 | 客户温度（活跃度）/ 客户价值，客户资源库中的标签 |
| DO留痕 | 操作记录同步至平安DO系统留存 |
| 经营日历 | 按考核节点排布的月度/季度计划时间轴 |

## 当前进度

- [x] 产品功能架构图 V1.0 完成
- [x] 首页 AskBob 入口 PRD 完成
- [x] 平安DO 首页原型图 v0.5 完成
- [ ] 智能体详细交互流程设计
- [ ] MCP 工具接口定义
- [ ] 各功能模块原型细化

## 备注

- 本智能体定位为**内勤侧**工具，非代理人端（C端）工具
- 架构图版本：V1.0 · 2026年4月
- 原型版本：v0.5

---

## PC 端原型 UI 规范（AskBob 对话页）

> 适用文件：`原型图/PC端20260530版本.html`
> 规范版本：v1.0 · 2026年5月

---

### 一、色彩系统

| Token | 值 | 用途 |
|---|---|---|
| Primary | `#2563eb` | 主色：按钮、选中态、链接、发送键 |
| Primary-light | `#3b82f6` | 浅主色：hover 边框、focus ring |
| Primary-dark | `#1e40af` | 深主色：hover 按钮背景 |
| BG-deep | `#0f172a` | 顶部导航栏背景 |
| BG-nav | `#1e293b` | 导航层次背景 |
| BG-sidebar | `#f8fafc` | 左侧边栏背景、卡片次级区域 |
| BG-main | `#f1f5f9` | 页面主背景、右侧栏背景 |
| BG-card | `#ffffff` | 卡片背景、输入框背景 |
| BG-chat | `#fafbfd` | 聊天消息区背景 |
| Text-primary | `#1e293b` | 主文本、标题 |
| Text-secondary | `#64748b` | 正文、次级说明 |
| Text-muted | `#94a3b8` | 辅助文本、占位符、图标 |
| Border | `#e2e8f0` | 通用边框 |
| Border-light | `#f1f5f9` | 卡片内部分隔线 |
| Accent-orange | `#f59e0b` | 警告、待办 |
| Accent-green | `#10b981` | 成功、新增 |
| Accent-red | `#ef4444` | 危险、脱落、退出按钮 |
| Shadow-sm | `0 1px 2px rgba(0,0,0,0.05)` | 卡片阴影 |
| Shadow-md | `0 4px 12px rgba(0,0,0,0.08)` | 悬浮卡片阴影 |
| Shadow-lg | `0 8px 24px rgba(0,0,0,0.12)` | 模态/全屏阴影 |

> **禁止**使用渐变色边框（border-image/gradient border）。渐变仅用于顶部导航底部分隔线装饰。

---

### 二、字体规范

**字体族**：`'Noto Sans SC', -apple-system, BlinkMacSystemFont, sans-serif`

| 层级 | 大小 | 字重 | 颜色 | 用途 |
|---|---|---|---|---|
| Page Title | 18px | 700 | Text-primary | 首页卡片标题（AskBob、经营数据看板） |
| Section Title | 16px | 700 | `#333` | 看板标题（经营数据看板、人力看板） |
| Nav Logo | 16px | 600 | `#fff` | 顶部导航 Logo 文字 |
| Sidebar Brand | 18px | 700 | Text-primary | 左侧栏 "AskBob" 品牌名 |
| Body | 14px | 400 | Text-primary | 导航菜单、侧边栏导航项、输入框 |
| Card Body | 13.5px | 400 | Text-primary | AI/用户气泡消息正文，行高 1.7 |
| Label | 13px | 500/600 | Text-secondary | 聊天历史条目、Panel 标题、输入 placeholder |
| Meta | 12px | 400/500 | Text-secondary | 推荐问 chips、快捷提示 chips |
| Caption | 11–12px | 400/500 | Text-muted | 辅助说明、数据单位、徽标 |
| Micro | 10–11px | 400 | Text-muted | 图例标签、次级注释 |

**基准字号**：`body { font-size: 14px }`

> **禁止**对中文使用 `font-style: italic`。

---

### 三、整体布局

```
┌─────────────────────────────────────────────────────┐
│  Top Nav (52px)  bg-deep #0f172a                    │
├────────────┬───────────────────────────┬────────────┤
│ Left       │  Center Panel (flex:1)    │ Right      │
│ Sidebar    │  bg-main → chat-frame     │ Sidebar    │
│ 260px      │  (白色卡片)               │ 240px      │
│ bg-sidebar │  padding: 16px            │ bg-main    │
└────────────┴───────────────────────────┴────────────┘
```

- `app-body` 高度 = `calc(100vh - 52px)`，`overflow: hidden`
- 左侧栏可折叠至 52px（icon-only rail），过渡 `width 0.25s ease`
- 中区 `chat-frame`：`border: 1px solid border`，`border-radius: 12px`，`background: white`

---

### 四、顶部导航（Top Nav）

| 元素 | 规格 |
|---|---|
| 高度 | 52px |
| 背景 | `#0f172a`（BG-deep） |
| 底部装饰线 | `linear-gradient(90deg, transparent, rgba(59,130,246,0.5), transparent)` 高度 1px |
| Logo 图标 | 32×32px，`border-radius:8px`，Primary→#60a5fa 渐变，"DO" 15px/700 白色 |
| Logo 文字 | 16px/600 白色 |
| Logo 副文字 | 10px `rgba(255,255,255,0.4)` |
| 导航链接（非激活） | 13px/400，`rgba(255,255,255,0.6)`，hover 0.9 |
| 导航链接（激活） | 13px/500，白色；底部 2px `#3b82f6` 下划线，`border-radius:2px 2px 0 0` |
| 右侧图标 | 18×18px SVG，`opacity:0.5`，hover `0.9` |
| 头像圈 | 28×28px，Primary→#60a5fa 渐变 |
| 用户名 | 13px `rgba(255,255,255,0.7)` |

---

### 五、左侧边栏（对话模式）

| 元素 | 规格 |
|---|---|
| 宽度 | 260px（折叠后 52px） |
| 背景 | `#f8fafc`（BG-sidebar） |
| 右边框 | `1px solid #e2e8f0` |
| 品牌区（顶部） | 返回按钮 28×28px + "AskBob" 18px/700 + 折叠按钮 28×28px |
| 返回/折叠按钮 | `border-radius:6px`，transparent 背景，hover `rgba(0,0,0,0.05)` |
| 新建对话按钮 | dashed border `#e2e8f0`，14px/500，hover `border-color: text-muted` |
| 导航条目 | 14px/400，text-secondary，`padding:9px 10px`，`border-radius:8px`，hover `rgba(0,0,0,0.04)` |
| 导航图标 | 18×18px，`opacity:0.6` |
| 分隔线 | `height:1px`，`background:#e2e8f0`，`margin:18px 16px` |
| 区块标签 | 12px/500，text-muted，`padding:10px 16px 6px` |
| 历史条目（普通） | 14px，text-secondary，`border:1px solid transparent`，hover `rgba(0,0,0,0.04)` |
| 历史条目（激活） | `background:white`，`border-color:#e2e8f0`，`box-shadow:shadow-sm` |
| 滚动条 | 宽 4px，`background:#d4d4d4`，`border-radius:4px` |
| 退出按钮（在页内） | `border:1px solid border`，`border-radius:8px`，hover `background:#fef2f2 / border #fca5a5 / color accent-red` |

---

### 六、消息气泡

#### AI 气泡（`.msg-bubble.ai-bubble`）
- 背景：`#ffffff`；边框：`1px solid #e2e8f0`
- 圆角：`14px 14px 14px 4px`（左上为 14px，右上 14px，但规范中是 border-top-left-radius: 4px）
  即：`border-radius: 14px; border-top-left-radius: 4px`
- 内边距：`12px 16px`；最大宽度：85%
- 字号：13.5px，行高：1.7；颜色：text-primary
- 阴影：shadow-sm

#### 用户气泡（`.msg-bubble.user-bubble`）
- 背景：`#2563eb`（Primary）；文字：白色
- 圆角：`border-radius: 14px; border-top-right-radius: 4px`
- 内边距：`12px 16px`

#### 工具结果气泡（`.msg-bubble.tool-bubble`）
- 继承 ai-bubble 样式，`max-width: 75%; width: 75%`

**消息行动效**：`animation: msgIn 0.3s ease-out`（从 translateY(8px) + opacity 0 进入）

---

### 七、输入栏（Chat Input）

| 元素 | 规格 |
|---|---|
| 外层 padding | `12px 28px 16px` |
| 背景 | white；顶部 `1px solid border-light` |
| 输入框容器 | `border-radius:14px`，`border:1px solid #e2e8f0`，`padding:6px 6px 6px 16px` |
| 输入框 focus | `border-color:#3b82f6`，`box-shadow:0 0 0 3px rgba(59,130,246,0.12)` |
| 输入文本 | 14px，text-primary，placeholder text-muted |
| 图标按钮 | 34×34px，`border-radius:8px`，text-muted，hover `bg-sidebar` |
| 发送按钮 | 36×36px，`border-radius:10px`，Primary bg，`box-shadow:0 2px 8px rgba(37,99,235,0.3)` |
| 发送 hover | Primary-dark bg，`box-shadow:0 4px 12px rgba(37,99,235,0.4)`，`translateY(-1px)` |
| 停止按钮 | 36×36px，`#ef4444` bg，同尺寸，仅发送中显示 |
| 快捷 chips 行 | `margin-top:8px`，横向滚动，左右渐变遮罩，`border-radius:20px`，12px |
| Chip hover | `border-color:#3b82f6`，`color:primary`，`bg:#eff6ff` |

---

### 八、推荐问滚动区（Recommend Section）

- 位于消息区底部、输入栏顶部之间
- 内容水平自动轮播（`animation: recScrollLR 22s linear infinite`），hover 时暂停
- 左右遮罩：`mask-image: linear-gradient(90deg, transparent, #000 4%, #000 96%, transparent)`
- 每条 item：`border-radius:20px`，`bg:#f8fafc`，`border:1px solid #e2e8f0`，13px，text-secondary
- Hover：`bg:#eff6ff`，`border:#bfdbfe`，`color:primary`
- 每条末尾带箭头图标（opacity 0.4，hover 0.8）

---

### 九、思考卡片（Thinking Card）

- 背景：BG-sidebar；边框：`1px solid border`；`border-radius:8px`（radius-sm）
- Header：spinner 14×14px（`border-top-color: primary`）+ 状态文字 12px/500 text-muted
- Body：13px，text-secondary，行高 1.7；超出折叠（`max-height: 4.8em`）
- 展开/收起按钮：primary 色，12px/500，箭头旋转 180°
- 完成态：spinner 隐藏，顶部边框变绿（`#16a34a`）

---

### 十、选项卡片（Path Options）

#### 单选（Radio）
- 容器：`padding:8px 14px`，`border-radius:10px`，`border:1px solid #e2e8f0`
- 指示点：18×18px 圆形，选中 = Primary 填充 + 内部 6×6px 白色圆点
- 选中态：`border-color:#3b82f6`，`background:#eef2ff`，左侧 3px Primary 竖条
- Hover（未选中）：`border-color:#c7d2fe`，`background:#f8faff`，`translateX(2px)`

#### 多选（Checkbox）
- 指示框：18×18px，`border-radius:4px`（方形）
- 选中：Primary 填充 + 白色勾
- 多选确认按钮：`padding:7px 22px`，Primary bg，`border-radius:8px`，13px/600

---

### 十一、下一步推荐按钮（Next Step Buttons）

| 类型 | 样式 |
|---|---|
| 基础款 | `border:1px solid #e2e8f0`，`border-radius:8px`，`padding:9px 12px`，12px/500，text-secondary |
| Hover | `border-color:#3b82f6`，`color:primary`，`bg:#f8faff` |
| 原子工具类 | 左侧 `3px solid primary`，`bg:#f8faff`，hover `bg:#eef2ff` |
| 跟进类 | `border-style:dashed`，`border-color:text-muted`，hover 实线 |

---

### 十二、看板数据卡片

- 外容器：`border-radius:12px`，`border:1px solid #e2e8f0`，`padding:12px 14px`，shadow-sm
- Panel 标题：`13px/600`，text-primary，底部 `1px solid border-light`
- Panel 图标：24×24px，`border-radius:6px`，BG 色块（业务=`#fff7ed`，人力=`#eff6ff`）
- KPI 大数字：18–22px/700，text-primary；单位 12px/400 text-muted
- 图例点：7×7px 圆形

---

### 十三、首页 AskBob 入口区

| 元素 | 规格 |
|---|---|
| 卡片背景 | `#ffffff`，`border-radius:4px` |
| 卡片宽度 | 左 68%（AskBob+待办）/ 右 32%（快捷入口） |
| "AskBob" 标题 | 18px/700，`#333` |
| 副标题 | 12px，`#999` |
| "进入AskBob" 按钮 | `border-radius:20px`，`border:none`，渐变背景 `linear-gradient(135deg,#2563eb,#7c3aed)`，12px/500 白色，`box-shadow:0 2px 10px rgba(99,102,241,0.35)` |
| 推荐问区块标题 | "推荐问" 12px/500，"换一批" 12px 可点击 |
| 推荐问 Chips | `bg:#f8fafc`，`border:1px solid #ddd`，`border-radius:20px`，11px，hover = `border:#90caf9`，`color:#1976d2`，`bg:#e8f0fe` |
| 输入框 | textarea，`border:1px solid #e5e7eb`，`border-radius:8px` |
| 发送按钮（首页） | 圆形，Primary bg |
| 待办任务条目 | `bg:#fff8e1`，`border:1px solid #ffe0b2`，`border-radius:6px`，13px，截止日期橙色 |
| 快捷入口图标 | 22×22px SVG，`#1976d2` stroke，容器 40×40px `#f0f4ff` rounded |

---

### 十四、右侧边栏（AI 对话模式）

| 元素 | 规格 |
|---|---|
| 宽度 | 240px |
| 背景 | BG-main `#f1f5f9` |
| 无左边框 | — |
| 顶部标题 | 14px/600，text-primary，底部 `1px solid border-light` |
| 公告轮播（Notice carousel） | 自动切换，dot 指示器，宽 6px（激活态 16px 长条） |
| 快速功能 Grid | 3列，图标 34×34px，`bg:#eff6ff`，`border-radius:8px`；标签 10px，text-secondary |
| 图标 hover | `bg:#dbeafe`，`box-shadow:0 2px 8px rgba(37,99,235,0.15)`，`translateY(-2px)` |

---

### 十五、交互规范

| 行为 | 实现方式 |
|---|---|
| 进入对话 | `#aiAppBody.style.display = 'flex'`；隐藏首页 |
| 返回首页 | `goBackToHomepage()`；首页重新显示 |
| 侧边栏折叠 | `.sidebar-left.classList.toggle('collapsed')`；icon-only rail |
| 新建对话 | 清空历史消息，仅保留 Welcome 消息 |
| 发送消息 | 用户气泡立即渲染 → 思考卡片 → 结果卡渲染 |
| 停止生成 | `#stopBtn` 显示（`.visible`），点击终止 |
| 全屏看板 | `position:fixed`，`z-index:1000`，overlay `rgba(0,0,0,0.4)` |
| 输入框 focus | Primary-light 边框 + 半透明 focus ring |
