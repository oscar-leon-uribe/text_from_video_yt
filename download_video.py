from pytube import YouTube
url = 'https://www.youtube.com/watch?v=XD0hUkE__ps'
name = url.split('=')[1]
yt = YouTube(url)
video = yt.streams\
    .filter(file_extension='mp4')\
    .first()\
    .download(output_path='videos', filename=url.split('=')[1])
