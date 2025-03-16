# 这段函数是用ffmpeg将图标压缩至32x32格式，与web无关。
import subprocess

def compress_image(input_file, output_file, width=32, height=32):
    
    command = [
        'ffmpeg',
        '-i', input_file,          
        '-vf', f'scale={width}:{height}',  # 缩放图像
        output_file                
    ]
    
    # 执行命令
    subprocess.run(command, check=True)


input_file = './blog-sign.png'
output_file = './output_32x32.png'
compress_image(input_file, output_file)