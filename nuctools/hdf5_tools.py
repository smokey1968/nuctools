import numpy as np
import h5py as h5
import time
import warnings

__all__ = ['printname','check_hdf5_triggers']

def printname(name):
    """ 
    Print whatever is given for name 
    
    Parameters
    ----------
    name : object
        Any printable object

    Returns
    -------
    no return : 
        print statement

    """

    print(name)

def check_hdf5_triggers(hdf5_folder,sample_name):
    """
    Interrogate a standard format RPI linac HDF5 file to compare the 
    triggers recorded by the scaler and the TDC events in the data 
    collection

    Parameters
    ----------
    hdf5_folder : str
        The full filepath where the file lives. Example: "/C:/Data/08Aug17/"
        Should end with a slash
    sample_name : str
        The name sample name associated with the file. This should be in format:
        {name}_master.h5, and *inside* the file, it should start with heading
        name. for example: B4C/CYCLE0001/MON/ and B4C/CYCLE0001/TRIG/ should be 
        paths within the file.

    Returns
    -------
    no return : 
        print statement

    Notes
    -----
    This function is highly dependent on the structure of the datasets in the 
    HDF5 file. This means that users should be very careful when applying this
    to their own data.

    """

    # Warning should be left in until this has been solved.
    warnings.warn("\n\nThis function is requires rigid dataset structure. See notes.\n\n")

    with h5.File("{}{}_master.h5".format(hdf5_folder,sample_name,'r')) as hdf:
        # set stuff to be saved -----------------------------------------------
        percent_diff_array = np.zeros(len(hdf["{}".format(sample_name)]))
        bad_cycles = []
        # ---------------------------------------------------------------------
        for i,cycle in enumerate(hdf["{}".format(sample_name)]):
            mon = np.array(hdf["{}/{}/MON".format(sample_name,cycle)])
            trig = np.array(hdf["{}/{}/TRIG".format(sample_name,cycle)])
            expected_trig = trig[0][0]
            percent_diff = abs(mon[7]-trig[0][1])/((mon[7]+trig[0][1])/2)*100
            # should the percent diff be recorded? ----------------------------
            condition1 = (percent_diff > 100)
            condition2 = (float(trig[0][1])<expected_trig/2)
            condition3 = (float(mon[7])<expected_trig/2)

            if (condition1 or condition2 or condition3):
                print("WARNING: Large trigger difference detected in CYCLE",i)
                percent_diff = 0
                bad_cycles.append('CYCLE '+str(i))
            # print out for the user ------------------------------------------
            print(i+1,"Scal/TDC trigs ===>",mon[7],"/",trig[0][1],
                  "  % Diff: {:.4f}".format(percent_diff))
            percent_diff_array[i] = percent_diff
    
        print("----------------------------")
        print("AVG perc. diff.: {:.4f}%".format(percent_diff_array.mean()))
        print("STD of perc. diff.: {:.4f}".format(percent_diff_array.std()))
        print("----------------------------")
        print("CYCLES that should probably be thrown out (set to 0%):")
        for bad_cycle in bad_cycles:
            print(bad_cycle)
        print("----------------------------")


