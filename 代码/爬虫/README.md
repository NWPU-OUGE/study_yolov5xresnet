# 爬虫功能说明

* 通过PYTHON抓取直播流并通过ffmpeg将直播流截图，合并转换格式。直播流常见文件格式有ts流，flv流，m3u8流。本方案支持抓取以上全部三种格式的视频流，只需在调用ffmpeg时略微修改参数即可。

* 目录包含以下文件：

  * ffmpeg.exe 格式转换与截图
  
  * run.bat  用于调用ffmpeg
  
  * get-real-url.py 获取直播流真实地址
  
  * download-url.py 下载直播流文件
  

solution by 唐天扬 

