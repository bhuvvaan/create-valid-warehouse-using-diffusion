# Creating valid warehouses

A _valid warehouse layout_ is a special kind of layout that follows certain rules. For more information, refer to [https://arxiv.org/abs/2305.06436](https://arxiv.org/abs/2305.06436). 

This repo contains code that creates those warehouse environments using diffusion models. It uses huggingface APIs to train a diffusion model from scratch. 

```using_diffusers_on_numpy_arrays.ipynb``` can be run by itself without any dependencies. The code also generates its own training data and trains the model.

## Depth first approach to create the training data

```dfs.py``` is the logic that creates the training data. The warehouse layout needs to follow certain physical rules and DFS was used to acheive this. ```using_diffusers_on_numpy_arrays.ipynb``` uses a fixed dimension warehouse, to change the dimension, the DFS logic in it needs to be changed.

## Chain of thought approach

A Chain of thought approach was also tried to achieve the warehouse layout that follows the constraints that were preveiously mentioned. OpenAI's API was used for this approach. Although the results were not satisfactory, the code can be found at ```chain_of_thought.py```. It will require an OpenAI API key.

