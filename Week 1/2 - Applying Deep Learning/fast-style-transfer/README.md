# Style Transfer
Add styles from famous paintings to any photo in a fraction of a second! And even for videos.

Pull Source code from this repo first - https://github.com/lengstrom/fast-style-transfer

Few checkpoints are available in Checkpoints folder.
For more checkpoints - https://drive.google.com/drive/folders/0B9jhaT37ydSyRk9UX0wwX3BpMzQ

Sample input and output added to Resources folder

Setting up the environment:
```
conda create -n style-transfer python=2.7.9
source activate style-transfer
conda install -c conda-forge tensorflow=0.11.0
conda install scipy pillow
```

For style transfer:
```
python evaluate.py --checkpoint ./rain-princess.ckpt --in-path <path_to_input_file> --out-path ./output_image.jpg
```
