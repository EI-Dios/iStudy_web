# Django web开发iStudy学习平台
## 效果图
注册：
![](https://github.com/EI-Dios/iStudy_web/blob/master/iStudy/static/images/projet_images/%E6%B3%A8%E5%86%8C.png)
登录：
![](https://github.com/EI-Dios/iStudy_web/blob/master/iStudy/static/images/projet_images/%E7%99%BB%E5%BD%95.png)
主页：
![](https://github.com/EI-Dios/iStudy_web/blob/master/iStudy/static/images/projet_images/%E4%B8%BB%E9%A1%B5.png)
评论页面：
![](https://github.com/EI-Dios/iStudy_web/blob/master/iStudy/static/images/projet_images/%E8%AF%84%E8%AE%BA%E9%A1%B5%E9%9D%A2.png)
个人管理中心_文章管理：
![](https://github.com/EI-Dios/iStudy_web/blob/master/iStudy/static/images/projet_images/%E4%B8%AA%E4%BA%BA%E7%AE%A1%E7%90%86%E4%B8%AD%E5%BF%83_%E6%96%87%E7%AB%A0%E7%AE%A1%E7%90%86.png)
个人管理中心_分类管理：
![](https://github.com/EI-Dios/iStudy_web/blob/master/iStudy/static/images/projet_images/%E4%B8%AA%E4%BA%BA%E7%AE%A1%E7%90%86%E4%B8%AD%E5%BF%83_%E5%88%86%E7%B1%BB%E7%AE%A1%E7%90%86.png)
## 开发工具：
- pycharm
- python语言
- Djang框架
- MySql(ORM)
## 项目简介
> 基于Django框架开发一个学习平台。用ORM语句创建数据库，modelform实现注册，用局部钩子和全局钩子校验注册信息是否符合规范，注册的时候还可以上传头像。在主页可以看到数据库中所有文章标题和摘要，点击可以看到文章详情。通过中间件查看登录状态，若登录就可以在文章下面评论，还可以进入个人管理中心进行文章管理和分类管理；若没登录则跳转到登录页面，登录成功后返回用户想要前往的页面。在个人管理中心可以通过模糊查询查找某篇文章，可以增加或编辑文章，最后再实现分页功能，分页保留查询参数。
