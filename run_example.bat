@echo off
powershell -Command "& {conda activate whisperx; python 'D:\Project\whisperX\movie-to-ass.py' '%1'}"

