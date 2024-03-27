from moviepy.editor import VideoFileClip

def extract_audio(video_file_path, audio_file_path):
    # 加载视频文件
    video = VideoFileClip(video_file_path)

    # 提取音频
    audio = video.audio

    # 保存音频为WAV
    audio.write_audiofile(audio_file_path, codec='pcm_s16le')  # 指定WAV格式的编解码器

    # 释放资源
    audio.close()
    video.close()

# 使用示例
# video_file_path = r'D:\Project\whisperX\whisperx\translate\example\test.mp4'  # 视频文件路径
# audio_file_path = r'D:\Project\whisperX\whisperx\translate\example\test.wav'  # 输出的音频文件路径（WAV格式）
# extract_audio(video_file_path, audio_file_path)
