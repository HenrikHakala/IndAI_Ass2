import os
import json

class CircuitBoardSolver(object):
    CLSNAMES = ['circuitboard']

    def __init__(self, root='D:\\Cursor projects\\Assignment2\\CLIP\\Anomaly\\Data'):
        self.root = root
        self.meta_path = os.path.join(root, 'meta.json')

    def run(self):
        info = dict(train={}, test={})
        anomaly_samples = 0
        normal_samples = 0

        for cls_name in self.CLSNAMES:
            cls_dir = f'{self.root}/{cls_name}'
            for phase in ['train', 'test']:
                cls_info = []
                if phase == 'train':
                    species = ['good']
                else:
                    species = ['good', 'broken']

                for specie in species:
                    is_abnormal = specie != 'good'
                    img_dir = f'{cls_dir}/{phase}/{specie}'
                    if not os.path.exists(img_dir):
                        continue
                    img_names = os.listdir(img_dir)
                    img_names.sort()
                    for img_name in img_names:
                        if is_abnormal and phase == 'test':
                            base_name = os.path.splitext(img_name)[0]
                            mask_name = base_name + '_mask.png'
                            mask_path = f'{cls_name}/ground_truth/{specie}/{mask_name}'
                        else:
                            mask_path = ''
                        info_img = dict(
                            img_path=f'{cls_name}/{phase}/{specie}/{img_name}',
                            mask_path=mask_path,
                            cls_name=cls_name,
                            specie_name=specie,
                            anomaly=1 if is_abnormal else 0,
                        )
                        cls_info.append(info_img)
                        if phase == 'test':
                            if is_abnormal:
                                anomaly_samples += 1
                            else:
                                normal_samples += 1
                info[phase][cls_name] = cls_info

        os.makedirs(os.path.dirname(self.meta_path), exist_ok=True)
        with open(self.meta_path, 'w') as f:
            json.dump(info, f, indent=4)

        print('✅ JSON generated.')
        print('Normal test samples:', normal_samples)
        print('Anomalous test samples:', anomaly_samples)


if __name__ == '__main__':
    runner = CircuitBoardSolver(root='D:\\Cursor projects\\Assignment2\\CLIP\\Anomaly\\Data')
    runner.run()
