from random import randint, sample
import numpy as np
import matplotlib.pyplot as plt

global group_size_max
group_size_max = 200

def create_array(length):
    array = []
    for i in range(length):
        array.append(i)
    return array

def shuffle_array(array):
    shuffeled = sample(array, len(array))
    return shuffeled

def check_arrays(array1, array2):
    for i in range(len(array1)):
        if array1[i] == array2[i]:
            #print(array1[i], array2[i])
            return False
    return True

def run_one_test(length):
    array1 = create_array(length)
    array2 = shuffle_array(array1)
    return check_arrays(array1, array2)

def test_series(length):
    passed = 0
    failed = 0

    for i in range(10000):
        if run_one_test(length):
            passed += 1
        else:
            failed += 1
    
    #print("Passed: ", passed)
    #print("Failed: ", failed)
    #print("Total: ", passed + failed)
    #print("Percentage: ", passed / (passed + failed))

    return passed / (passed + failed)

def run_tests(min, max):
    dict = {
    }

    for i in range(min, max):
        dict[i] = test_series(i)

    return dict

def plot_results(dict):
    global group_size_max
    plt.plot(dict.keys(), dict.values(), color='green', linestyle='dashed', linewidth = 3, marker='o', markerfacecolor='blue', markersize=12)
    m, b = np.polyfit(list(dict.keys()), list(dict.values()), 1)

    regression_line = []
    for i in range(len(dict)):
        regression_line.append(m * (list(dict.values())[i]) + b)

    plt.plot(dict.keys(), regression_line, color='red')
    plt.title('Wahrscheinlichkeit eigenen Namen zu ziehen')
    plt.xlabel('Größe der Gruppe [n]')
    plt.ylabel('Wahrscheinlichkeit eigenen Namen ziehen [p]')
    plt.text(group_size_max/5, 0.1, "Durchschnitt: " + str(round(np.average(list(dict.values())), 3)), fontsize=16)
    plt.show()

def main():
    global group_size_max
    dict = run_tests(1, group_size_max)
    print(dict)
    plot_results(dict)


main()