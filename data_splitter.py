def get_subset(image_path, data_splits=["train","test","valid"],
              amount=[0.6,0.3,0.1],seed=42): 
    random.seed(42)
    label_splits = {}

    # Get labels
    i=0
    for data_split in data_splits:
        label_dir_name = ip / f"{data_split}.txt"
        if not label_dir_name.is_dir():
            print(f"[INFO] Creating image path for: {data_split}...")
            label_path = Path(label_dir_name)
            label_path.mkdir(parents=True, exist_ok=True)
            
            with open(ip, "r") as f:
                labels = [line.strip("\n") for line in f.readlines()]

            # Get random subset of image ID's
            num_sample = round(amount[i]*len(labels))
            print(f"[INFO] Getting random subset of {num_sample} images for {data_split}...")
            sampled_images = random.sample(labels, k=num_sample)
    
            # Apply full paths
            im_paths = [Path(str(ip / sample_image) + ".jpg") for sample_image in sampled_images]
            label_splits[data_split] = im_paths
            
        else: 
            print(f"[INFO] Path already exists for: {data_split}. Continuing...")
        i += 1
    return label_splits

#current split: train 0.6, test 0.3, valid 0.1
label_splits = get_subset()

#actually copying data over to train/test/valid folders.....

for image_split in label_splits.keys():
    for im_path in label_splits[str(image_split)]:
        pass
    pass


'''
import shutil

for image_split in label_splits.keys():
    for image_path in label_splits[str(image_split)]:
        dest_dir = target_dir / image_split / image_path.parent.stem / image_path.name
        if not dest_dir.parent.is_dir():
            dest_dir.parent.mkdir(parents=True, exist_ok=True)
        print(f"[INFO] Copying {image_path} to {dest_dir}...")
        shutil.copy2(image_path, dest_dir)

from https://github.com/mrdbourke/pytorch-deep-learning/blob/main/extras/04_custom_data_creation.ipynb
'''