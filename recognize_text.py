import os
import io
import sys
from google.cloud import videointelligence
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'credentials/keys.json'
### Enter as arguments video_id and number of text fragments
video_id = str(sys.argv[1])
n = int(sys.argv[2])

video_client = videointelligence.VideoIntelligenceServiceClient()
features = [videointelligence.Feature.TEXT_DETECTION]
video_context = videointelligence.VideoContext()
path = 'videos/'+video_id+'.mp4'
with io.open(path, "rb") as file:
    input_content = file.read()

operation = video_client.annotate_video(
    request={
        "features": features,
        "input_content": input_content,
        "video_context": video_context,
    }
)
result = operation.result(timeout=300)
annotation_result = result.annotation_results[0]

texts = []
count = []
for text_annotation in annotation_result.text_annotations:
    texts.append(text_annotation.text)
    count.append(len(text_annotation.segments))
values = dict(zip(texts, count))
sorted_values = sorted(values.items(), key=lambda kv: kv[1], reverse=True)
if n > len(sorted_values):
    print('Exceeded the number of phrases in the video')
else:
    print(list(sorted_values)[0:n], sep='\n')


