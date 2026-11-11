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


import numpy as np
import matplotlib.pyplot as plt

#调整到最接近RAS的轴方向
img_ras = nib.as_closest_canonical (img) 
#调整数组的轴顺序以及必要的返回在哪，同属更新affine，使其最接近RAS方向，本身不执行重采样

#获取Numpy数组
mri = img_ras.get_fdata(
    dtype=np.float32,
    caching="unchanged"
)

#确保是三维数组
if mri.ndim !=3:
    raise ValueError("Expected a 3D MRI")

#取第三个轴的中间切片
middle = mri.shape[2]//2
sliced_2d = mri[:,:,middle]

#显示图像
plt.imshow(sliced_2d,cmap="gray",origin="lower")
plt.title("T1CE-Middle Slice")
plt.axis("off")
plt.show()

#nib.load()创建图像对象，不仅包含MRI图像数据，还包含图像的空间数据
#get_fdata()用于后续的图像处理，默认使用float64，如果需要float32，需要指定dtype=np.float32,对于大体积MRI尤其重要
#你的MRI数据有多大？
#176x464x512=41,811,968个体素
#如果使用float64，约319Mib，如果是32，约159.5Mib，因此，后续读取MRI优先使用：
mri = img.get_fdata(dtype = np.float32,caching="unchanged")
#caching="unchanged"避免主动填充Nibabel图像对象内部的数据缓存，以上是CPU的内存占用

#region
####理解Affine####
#如果我知道MRI某个提速的数组位置，如何知道它在患者物理空间内的实际坐标？
#affine是一个4x4的空间矩阵，将体素索引坐标转换为空间坐标

import nibabel as nib
import numpy as np
img = nib.load(str(mri_path))
img_ras = nib.as_closest_canonical(img)
mri = img_ras.get_fdata(
    dtype=np.float32,
    caching="unchanged"
)
print("Affine:")
print(img_ras.affine)
print("spacial units:")
print(img_ras.header.get_xyzt_units())
ijk = np.array(np.array([
    mri.shape[0] // 2,
    mri.shape[1] // 2,
    mri.shape[2] // 2
]))
xyz = nib.affines.apply_affine(
    img_ras.affine,
    ijk
) #将MRI数组中的这个位置转换成对应的RAS+物理空间坐标

print("Voxel coordinate:",ijk) #数组索引坐标
print("World cordinate:",xyz) #物理空间坐标，RAS+空间坐标系
print("Orientation:",nib.aff2axcodes(img_ras.affine))

#endregion

#region MRI三视图和空间方向
import matplotlib.plot as plt

i=mri.shape [0]//2
j = mri.shape[1]//2
k = mri.shape[2]//2

axial = mri[:,:,k]
coronal = mei[:.j.:]
sagittal = mri[i,:,:]

print("Axial:",axial.shape)
print("Coronal:",coronal.shape)
print("Sagittal:",sagittal.shape)

