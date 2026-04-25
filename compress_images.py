import os
from PIL import Image
import concurrent.futures

SOURCE_DIR = r"D:/Program Files/Obsidian/乙的知识库/02 Resources资料/摄影作品集/images"
OUTPUT_DIR = r"D:/Program Files/Obsidian/乙的知识库/02 Resources资料/摄影作品集/images_optimized"

# 目标：最长边1920px，质量85%，适合网页展示
MAX_SIZE = 1920
QUALITY = 85

def compress_image(filename):
    src_path = os.path.join(SOURCE_DIR, filename)

    # 跳过非图片文件和已删除的文件
    if not (filename.lower().endswith(('.jpg', '.jpeg', '.png'))):
        return None
    if filename == 'original-photo-01.png':
        return None

    try:
        img = Image.open(src_path)

        # 转换为RGB（处理PNG的RGBA）
        if img.mode in ('RGBA', 'P'):
            img = img.convert('RGB')

        # 获取原始尺寸
        orig_width, orig_height = img.size
        orig_size = os.path.getsize(src_path) / 1024 / 1024  # MB

        # 按比例缩放
        if max(orig_width, orig_height) > MAX_SIZE:
            ratio = MAX_SIZE / max(orig_width, orig_height)
            new_width = int(orig_width * ratio)
            new_height = int(orig_height * ratio)
            img = img.resize((new_width, new_height), Image.LANCZOS)
        else:
            new_width, new_height = orig_width, orig_height

        # 保存为优化后的JPEG
        output_filename = os.path.splitext(filename)[0] + '.jpg'
        output_path = os.path.join(OUTPUT_DIR, output_filename)

        img.save(output_path, 'JPEG', quality=QUALITY, optimize=True)

        new_size = os.path.getsize(output_path) / 1024 / 1024  # MB
        savings = (1 - new_size / orig_size) * 100 if orig_size > 0 else 0

        return f"{filename}: {orig_size:.1f}MB -> {new_size:.1f}MB ({savings:.0f}% smaller)"

    except Exception as e:
        return f"{filename}: ERROR - {str(e)}"

def main():
    # 创建输出目录
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # 获取所有图片文件
    files = [f for f in os.listdir(SOURCE_DIR)
             if f.lower().endswith(('.jpg', '.jpeg', '.png'))
             and f != 'original-photo-01.png']

    print(f"找到 {len(files)} 张图片待压缩...")
    print(f"目标: 最长边 {MAX_SIZE}px, 质量 {QUALITY}%")
    print("-" * 50)

    # 并行处理
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(compress_image, files))

    # 输出结果
    total_orig = 0
    total_new = 0
    for r in results:
        if r:
            print(r)
            # 解析大小计算总量
            parts = r.split(': ')[1].split(' -> ')
            total_orig += float(parts[0].replace('MB', ''))
            total_new += float(parts[1].split('MB')[0])

    print("-" * 50)
    print(f"总计: {total_orig:.1f}MB -> {total_new:.1f}MB")
    print(f"节省: {total_orig - total_new:.1f}MB ({(1-total_new/total_orig)*100:.0f}%)")
    print(f"\n优化后的图片保存在: {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
