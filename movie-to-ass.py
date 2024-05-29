from whisperx.translate.llamaapitest import translate2ch
import os
import sys
from pathlib import Path
from whisperx.translate.movie2audio import extract_audio
from whisperx.translate.srt2ass import srt_to_ass

# 接收参数传递
# print(sys.argv[1])
# video_path = sys.argv[1]
#
# ROOTDIR = Path(video_path)
ROOTDIR = Path("F:\File\Video\example")

for i in os.listdir(ROOTDIR):
    # 删除除wav以外的文件
    if not i.endswith(('.wav', '.mp4')):
        os.remove(ROOTDIR / i)

for i in os.listdir(ROOTDIR):
    if i.endswith('.mp4'):
        # 设置视频目录和输出音频目录
        file_path = str((ROOTDIR / i).absolute())
        audio_file_path = str((ROOTDIR / i).absolute()).replace('.mp4', '.wav')
        # 提取音频
        extract_audio(file_path, audio_file_path)
        # 运行语音识别
        os.system(rf"whisperx --model large-v2 --language ja --compute_type int8 {audio_file_path} -o {ROOTDIR.absolute()}")
        # 建立翻译文件，运行翻译
        trans_path = audio_file_path.replace('.wav', '.txt')
        translate2ch(trans_path)
        print(f"翻译结果已成功写入到文件")
        # 将srt文件转换为ass文件
        srt_file_path = trans_path.replace('.txt', '.srt')
        ass_file_path = trans_path.replace('.txt', '.ass')
        srt_to_ass(srt_file_path, ass_file_path)
        print(f"成功生成ass文件")


