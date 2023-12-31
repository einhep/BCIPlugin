import mne
import os

current_file_path = os.path.abspath(__file__)
current_dir_path = os.path.dirname(current_file_path)

BCIC_dir = current_dir_path+"\\test_data\\BCICdatasets"
mne_path = current_dir_path+"\\test_data\\mne_data"
EEGLABDIR = current_dir_path+"\\test_data\\eeglab_data"



mne.set_config("MNE_DATA", mne_path)
mne.set_config("MNE_DATASETS_ALEXEEG_PATH", mne_path)
mne.set_config("MNE_DATASETS_BNCI_PATH", mne_path)
mne.set_config("MNE_DATASETS_BRAININVADERS_PATH", mne_path)
mne.set_config("MNE_DATASETS_EEGBCI_PATH", mne_path)
mne.set_config("MNE_DATASETS_GIGADB_PATH", mne_path)
mne.set_config("MNE_DATASETS_MAMEM1_PATH", mne_path)
mne.set_config("MNE_DATASETS_MAMEM2_PATH", mne_path)
mne.set_config("MNE_DATASETS_MAMEM3_PATH", mne_path)
mne.set_config("MNE_DATASETS_NAKANISHI_PATH", mne_path)
mne.set_config("MNE_DATASETS_SSVEPEXO_PATH", mne_path)
mne.set_config("MNE_DATASETS_WANG_PATH", mne_path)


# For Unity BCIPlugin
MItype = {
    0: "LeftHand",
    1: "RightHand",
    2: "Tongue",
    3: "LeftFoot",
    4: "RightFoot",
    5: "Rest",
}
