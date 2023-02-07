import os
import cv2


class MiraclVc1:
    def __init__(self, id, sex, imgs):
        self.id = id
        self.sex = sex
        self.imgs = imgs

    @staticmethod
    def load_dataset(type, global_path="MIRACL-VC1"):
        if type != "words" and type != "phrases":
            raise ValueError("Type must be words or phrases")

        index_person = 1

        global_dir = os.listdir(global_path)
        # Entering person folder
        person_obj = []
        for i, person in enumerate(global_dir):
            print("Perform " + person + " " + str(index_person) + "/" + str(len(global_dir)))
            person_path = global_path + "/" + person + "/" + type
            sex = person[0]
            # print(os.listdir(dir))
            words_folder = os.listdir(person_path)
            # Entering words folder
            words_obj = []
            for word in words_folder:
                words_path = person_path + "/" + word

                label = word
                # print(os.listdir(words_folder))
                versions_folder = os.listdir(words_path)
                # Entering in frame folder
                frames_obj = []
                for version in versions_folder:
                    frames_path = words_path + "/" + version
                    frames_folder = os.listdir(frames_path)

                    index_version = version
                    for frame in frames_folder:
                        frame_path = frames_path + "/" + frame
                        frame_img = cv2.imread(frame_path)
                        frame_x = MiraclVc1.Word.Frame(str(frame[6:9]), frame_path, frame_img, frame[0:5], index_version)
                        frames_obj.append(frame_x)
                word_x = MiraclVc1.Word(label, label, frames_obj, words_path)
                words_obj.append(word_x)
            person_x = MiraclVc1(person, sex, words_obj)
            person_obj.append(person_x)
            index_person += 1

            if i > 0:
                break
        return person_obj

    class Word:
        def __init__(self, id, label, frame, path):
            self.id = id
            self.label = label
            self.frame = frame
            self.path = path

        class Frame:
            def __init__(self, index, path, frame, type, version):
                """
                    :type string c = color, d = depth
                """
                self.index = index
                self.path = path
                self.frame = frame
                self.type = type
                self.version = version