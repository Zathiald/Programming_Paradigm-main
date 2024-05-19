# Programming_Paradigm

## Context

For this problem we must imagine that we are part of a scientific team, and we are trying to investigate crystal structures at a molecular level in order to analyze and optimize molecules. This scientific team is now developing a new technique to imagine the crystal structures. The technique invovles blowing a very fine wind over the surface of the crystan at various angles in order to detect boundaries, this by knowing the molecules that are exposed to the wind. This process is repetead with different wind directions and we register each of the boundaries found. The team has already collected the data, but now the analysis must begin.

For a given crystal we are given the directions in which wind blew over the surface, and the locations of all boundaries encountered by each of these. For a wind blowing in direction (w_x, w_y), a boundary is defined as a location (x, y) such that a molecule exists at (x, y) and no molecule exists at (x - w_x, y - w_y).

We must find the two unique structures with the minimal and maximal number of molecules consistent with the observations. 

### Input

The first line of our input must contain three integers, d_x, d_y, and k, where d_x and d_y (1 ≤ d_x, d_y ≤ 10^3) are the maximum dimensions of the crystal structure, and k (1 ≤ k ≤ 10) is the number of times wind was blown over the crystal.

Each of the remaining k lines specifies the data for one wind. These lines each start with two integers w_x and w_y (-d_x ≤ w_x ≤ d_x and -d_y ≤ w_y ≤ d_y, but not both zero) denoting the direction of the wind. Then comes an integer b (0 ≤ b ≤ 10^5) giving the number of boundaries encountered by this wind. The line finishes with b distinct pairs of integers x, y (1 ≤ x ≤ d_x and 1 ≤ y ≤ d_y) listing each observed boundary.

### Output

Our output must be textual representations of the crystal structure separated by and empty line. Each structure has d_y rows of d_x characters, with the top-left corner corresponding to location (1, 1). The first is the structure with the minimal number of molecules consistent with the observations, the second is the maximal one. And we must use # for a location where a molecule exists and . for a location where no molecule exists.

## Model

## Implementation

## Testing

## Complexity

## Other Implementations

## References
