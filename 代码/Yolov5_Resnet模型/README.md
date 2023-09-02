# Yolov5_Resnet模型代码目录说明

该目录下的代码实现了**自动框出球和球员、裁判在画面中的位置，并以一张球场坐标图显示出他们在球场中的实际位置。**在backbone最后一层附加了SE注意力模型。

* Data目录用于存放需要推理的图片
* Detect_and_Track目录包含两步 1.通过Yolov5检测目标 2.通过Deep_Sort算法跟踪 由于时间原因Deep_Sort跟踪效率欠佳，默认注释
* Out目录用于存放推理后的结果
* projection_2D目录下包含了一个Resnet模型，用于得出一个投影矩阵来推出球员在球场上的实际位置。
* __ init __.py 文件 通过调用此文件运行我们的模型
* requirements.txt 文件 通过调用此文件来获得正确的依赖

