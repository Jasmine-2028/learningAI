from pathlib import Path
import nibabel as nib

#指定文件夹
mri_path = Path(r"E:\Test Data\standard_nii\a_2023_sub0003\\T1CE.nii.gz")
#检查文件
if not mri_path.is_file:
    raise FileNotFoundError(mri_path)

#读取nifTi图像
img = nib.load(str(mri_path))

print ("shape:",img.shape)
print("Voxel:",img.header.get_zooms()[:3]) #前三个值通常代表三个体素轴对应的采样间距，单位为mm。
print("Oritentation:",nib.aff2axcodes(img.affine))
print("Affine:")
print(img.affine)