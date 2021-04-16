import allure


def test_attach_text():
    allure.attach("这是一个纯文本", attachment_type=allure.attachment_type.TEXT)


def test_attach_html():
    allure.attach("<body>这是一段htmlbody块</body>", "html测试块", attachment_type=allure.attachment_type.HTML)


def test_attach_photo():
    allure.attach.file("/Users/guokairong/Downloads/工作文档/测试素材/图片/海贼/2da6d0be2ec4c95b7e035fc8a7654680.jpg",
                       name="这是一个图片", attachment_type=allure.attachment_type.JPG)


def test_attach_video():
    allure.attach.file("/Users/guokairong/Downloads/工作文档/测试素材/视频/0001.哔哩哔哩-【邓紫棋】 百事可乐2019 广告大片热爱全开_超清.mp4",
                       attachment_type=allure.attachment_type.MP4)
