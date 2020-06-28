import json
import os
from preproccess import tokenize

data_types = ['Friends']

DATA_PATH = os.path.join('./', 'data')
'''EMOTION = { 'neutral': 0, 
            'joy': 1, 
            'sadness': 2, 
            'anger': 3, 
            'fear': 4, 
            'surprise': 5, 
            'disgust': 6, 
            'non-neutral': 7}'''

def write_to_file(data_path, data_type, action, output_dir):
    assert action in ['train', 'dev', 'test']

    data_type = data_type.lower()
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    file_name = "{}_{}.json".format(data_type, action)
    with open(os.path.join(data_path, file_name), 'r') as f:
        source = json.load(f)

    utterance_lengths = []
    sentence_lengths = []

    all_utterance, all_emotion = [], []
    for n, diag in enumerate(source):
        utterance_lengths.append(len(diag))
        this_utterance, this_emotion = [], []
        for item in diag:
            utterance = tokenize(item['utterance'])
            emotion = item['emotion']
            this_utterance.append(utterance)
            this_emotion.append(emotion)
            sentence_lengths.append(len(utterance))

        all_utterance.extend(this_utterance)
        all_emotion.extend(this_emotion)

    with open(os.path.join(output_dir, "{}_{}.en".format(data_type, action)), 'w') as f:
        for line in all_utterance:
            f.write(line + '\n')
    with open(os.path.join(output_dir, "{}_{}.label".format(data_type, action)), 'w') as f:
        for line in all_emotion:
            f.write(line + '\n')

    print('Write {}.{} successfully ({} dialogues.)'.format(data_type, action, len(utterance_lengths)))

def merge_files(output_dir):
    for action in ['train', 'dev', 'test']:
        for kind in ["en", "label"]:
            file1 = os.path.join(output_dir, "{}_{}.{}".format("friends", action, kind))
            file_final = os.path.join(output_dir, "{}.{}".format(action, kind))
            os.system('cat %s > %s' % (file1, file_final))
    os.system('cat %s %s > %s' % (os.path.join(output_dir, "train.en"), os.path.join(output_dir, "dev.en"),
                                  os.path.join(output_dir, "data.en")))

def merge_files_with_tests(output_dir):
    os.system('cat %s %s > %s' % (os.path.join(output_dir,"train.en"), os.path.join(output_dir,"dev.en"), os.path.join(output_dir,"train-dev.en")))
    os.system('cat %s %s > %s' % (os.path.join(output_dir,"train.label"), os.path.join(output_dir,"dev.label"), os.path.join(output_dir,"train-dev.label")))
    os.system('cat %s %s %s > %s' % (os.path.join(output_dir, "train.en"), os.path.join(output_dir, "dev.en"), os.path.join(output_dir, "test.en"),
                                  os.path.join(output_dir, "data-all.en")))

if __name__ == '__main__':
    friend_data_path = os.path.join(DATA_PATH, 'Friends')
    output_dir = os.path.join(DATA_PATH, "preprocess_data")

    write_to_file(friend_data_path, 'Friends', 'train', output_dir)
    write_to_file(friend_data_path, 'Friends', 'dev', output_dir)
    write_to_file(friend_data_path, 'Friends', 'test', output_dir)

    merge_files(output_dir)
    merge_files_with_tests(output_dir)