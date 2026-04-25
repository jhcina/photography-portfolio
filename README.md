# 小乙哥的摄影作品集

一个杂志编辑风格的个人摄影作品展示网站。

## 预览

直接在浏览器中打开 `index.html` 即可预览网站。

## 如何添加你的照片

1. 在项目目录下创建 `images` 文件夹
2. 将你的照片放入该文件夹
3. 编辑 `index.html`，将 `.image-placeholder` 替换为实际的 `<img>` 标签

### 示例代码替换

将：
```html
<div class="image-placeholder">
    <div class="image-placeholder-icon"></div>
    <span>16:10 Image</span>
</div>
```

替换为：
```html
<img src="images/your-photo.jpg" alt="照片描述" style="width: 100%; height: 100%; object-fit: cover;">
```

## 网站结构

- **导航栏** - 固定顶部，包含关于我、作品集、联系链接
- **Hero区域** - 主标题和个人简介
- **作品展示区** - 杂志风格的不规则网格布局
- **关于我** - 个人介绍和摄影理念
- **页脚** - 联系方式和社交媒体链接

## 设计特点

- 杂志编辑风格排版
- Playfair Display 衬线字体
- 不规则网格布局
- 悬停动画效果
- 滚动渐入动画
- 响应式设计（支持桌面/平板/手机）

## 托管到 GitHub Pages

1. 在 GitHub 上创建新仓库（如 `photography-portfolio`）
2. 上传所有文件
3. 进入仓库 Settings → Pages
4. Source 选择 `main` 分支，点击 Save
5. 等待几分钟后，网站将发布到 `https://你的用户名.github.io/photography-portfolio`

## 技术栈

- HTML5
- CSS3 (CSS Grid, Flexbox, CSS Variables)
- Vanilla JavaScript
- Google Fonts (Playfair Display, Noto Sans SC, Cormorant Garamond)

---

© 2026 小乙哥
