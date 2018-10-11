# MMA Combo Assistant

### *Generates randomly ordered preset combos with configurable round lengths, added-in kicks, etc., and calls them out*

When first attending MMA classes one of the things discussed was the ability to flow between moves. A set of combos numbered 1 to 10 that the coach [Terry Riggs](https://www.warriormma.ca/) has written out is used to help this, and introduces some structure to fighting for beginners. The combos are as follows:

     
1. *Jab*
2. *Jab* **Cross**
3. *Jab* **Cross** *Hook*
4. *Jab* **Cross** *Hook* **Cross**
5. *Jab* **Cross** *Hook* **Cross** *Up*
6. **Cross**
7. **Cross** *Up*
8. **Cross** *Up* **Cross**
9. *Hook* **Cross** *Hook*
10. **Cross** *Hook*

With jabs, hooks, and uppercuts being done with the left, forward arm, and crosses being done with the right, rear arm ([Orthodox Stance](https://en.wikipedia.org/wiki/Orthodox_stance)).

In addition to these 10 combos, there are 20 further *Suggested Striking Combos* posted in the gym. As these are personally developed and named by Terry I feel it would be innappropriate to post them online. I *do* practice these combos with this tool but do not track them through Github (See [.gitignore](.gitignore)). 

## Usage
Simply clone the repository into your directory of choice, and install the required package:
```shell
pip install pygame
```
All other imported packages should be available by default with Python 3.x. Configure the parameters as desired and add in any combos to *basic_dict* before running, though the current configuration is fine to start with. Finally, run
```shell
python mma_callouts.py
```
from your terminal in the appropriate directory. The program will prompt for a desired number of rounds and will begin a countdown.

>*Note: [From Text to Speech](http://www.fromtexttospeech.com/) was used for the .mp3's found in [basic-files](basic-files) (I recommend either the Daisy or George voices at medium speed).*


## Configuration
### **Combo Dictionary Format**
```python
basic_dict = {
#   'combo-key': ['rel-path-to-mp3', 'rel-move-length', 'combo-moves']
    'one': ['./basic-files/one.mp3', 1, 'Jab']
# ...
}
```
> *Note: The relative move lengths were found through repeated trials. These may differ by user, but are intended primarily as ratios of the moves to each other based on the* time_weight *parameter.*

### **Parameters**
The following configuration parameters can be found in [config.py](config.py). As other users will not have access to the *riggs_system.py*, the *basic_rs_split* should be set to 1 to prevent missing file errors.

```python
time_weight = 875               # Time in ms alotted to 1 relative length unit for moves
time_const = time_weight/1000   # Constant used at varying points for time calculations
rest_length = 30                # Time in s of rests between rounds

kick_threshold = 0.3            # 70% of moves will have a kick appended
kick_length = 1                 # Relative length assigned to appended kicks
go_sk_split = 0.3               # 30% of appended kicks will be right kicks, 70% will be switch-kicks

basic_rs_split = 0.3            # 30% of combos will be from basic set, 70% will be from riggs system set
```
*I should realistically implement a check for riggs_system.py existing or else this parameter is set to 1; it's on the to do list*