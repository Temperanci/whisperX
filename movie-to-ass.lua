script_name = "自动化翻译脚本"
script_description = "识别语音翻译并输出ass"
script_version = "1.0"


--local io = require 'io'
--local os = require 'os'

function main(subtitles, selected_lines, active_line)
    -- 获取当前视频的路径
    local video_path = aegisub.project_properties().video_file
    aegisub.log("当前视频路径: %s\n", video_path)

    if video_path == "" then
        aegisub.log("错误：未加载视频！\n")
        return
    end

    -- 提取视频文件目录和文件名（不含扩展名）
    local video_dir = video_path:match("^(.*[/\\])")
    aegisub.log("当前视频目录: %s\n", video_dir)
    local video_filename = video_path:match("^.+[/\\](.+)%..+$")
    aegisub.log("当前视频名: %s\n", video_filename)
    local output_ass_path = video_dir .. video_filename .. ".ass"

    -- 构建运行run_example.bat的命令
    local command = 'cmd /c "D:\\Project\\whisperX\\run_example.bat "' .. video_dir .. '"'
    aegisub.log("运行命令：%s\n", command)

    -- 执行命令
    local result = os.execute(command)
    if result ~= 0 then
        aegisub.log("完成：py执行完毕。生成的双语ass字幕路径：%s\n", output_ass_path)
        return
    else
        aegisub.log("完成：py执行完毕。\n")
    end

    -- 检查生成的ASS文件是否存在
    --if not file_exists(output_ass_path) then
    --    aegisub.log("错误：未找到生成的ASS文件：%s\n", output_ass_path)
    --    return
    --end
    --
    --aegisub.log("尝试加载生成的ASS文件：%s\n", output_ass_path)
    --
    ---- 加载生成的ASS文件到Aegisub
    --aegisub.load_ass(output_ass_path)
    --aegisub.log("完成：ASS文件已加载。\n")
end


-- 检查文件是否存在的函数
function file_exists(path)
    local file = io.open(path, "r")
    if file then
        file:close()
        return true
    else
        return false
    end
end


aegisub.register_macro("自动化翻译脚本", "识别语音翻译并输出ass", main)
