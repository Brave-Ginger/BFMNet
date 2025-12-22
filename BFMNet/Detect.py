import sys
sys.path.append("/root/ultralytics")
from ultralytics import YOLO

if __name__ == '__main__':
    # 加载模型
    model = YOLO(r'C:\Users\PC\Desktop\runs\train\exp10\weights\weight.pt') 
    results = model(max_det=800)
model.predict(
    source=r'C:\Users\PC\Desktop\2222\cellpose',
    save=True,  # 保存预测结果
    imgsz=640,  # 输入图像的大小，可以是整数或w，h
    conf=0.3,  # 用于检测的目标置信度阈值
    iou=0.5,  # 降低IOU阈值，可能帮助边界框和分割掩码对齐
    show=False,  # 如果可能的话，显示结果
    project=r'C:\Users\PC\Desktop\2222',
    name='exp',
    save_txt=False,  # 保存结果为 .txt 文件
    save_conf=True,  # 保存结果和置信度分数
    save_crop=False,
    show_labels=True,
    show_conf=False,
    vid_stride=1,
    line_width=0,
    visualize=False,
    augment=False,
    agnostic_nms=False,
    retina_masks=True,  # 启用高分辨率分割掩码
    boxes=False,  # 显示边界框
    cache=True,  # (bool) True/ram、磁盘或False。使用缓存加载数据
)


