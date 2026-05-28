# Leon at SMHI

## Lotka-Volterra model

### Progonstic variables

- $x$ is the population density of preys (e.g. rabbits).
- $y$ is the population density of predators (e.g. foxes)

### Model parameters

- $\alpha = 1.0$: prey growth rate
- $\beta = 0.1$: prey death rate because of predators
- $\gamma = 0.75$: predators death rate
- $\delta = 0.075$: predators growth rate because of preys
- $\Delta t = 0.001$: time step

### Progonstic equations

- $x(t+\Delta t) = x(t) + (\alpha x(t) - \beta x(t) y(t)) \Delta t$
- $y(t+\Delta t) = y(t) + (-\gamma y(t) + \delta x(t) y(t)) \Delta t$

### Task: running the model
- Fork this repository on GitHub and clone it on your laptop.
- Use Python to implement the Lotka-Volterra model and run it over 30000 time steps. Save the results into NumPy arrays.
- Plot the results for each prognostic variable with Matplotlib.
- Save your code and results on GitHub.

## Lorenz 63 model

Source article: [Lorenz, E. N., 1963: Deterministic Nonperiodic Flow. J. Atmos. Sci., 20, 130–141](https://journals.ametsoc.org/view/journals/atsc/20/2/1520-0469_1963_020_0130_dnf_2_0_co_2.xml)

### Progonstic variables

- $x$ is proportional to the intensity of the convection (the rate of fluid flow).
- $y$ is proportional to the temperature difference between the rising and falling air currents.
- $z$ is proportional to the distortion of the vertical temperature profile from a linear one.

### Model parameters

- $\rho = 28$
- $\sigma = 10$
- $\beta = 8/3$
- $\Delta t = 0.01$: time step

### Progonstic equations

- $x(t+\Delta t) = x(t) + \sigma (y(t) - x(t)) \Delta t$
- $y(t+\Delta t) = y(t) + (\rho x(t) - y(t) - x(t) z(t)) \Delta t$
- $z(t+\Delta t) = z(t) + (x(t) y(t) - \beta z(t)) \Delta t$

### Task: running the model
- Fork this repository on GitHub and clone it on your laptop.
- Use Python to implement the Lorenz 63 model and run it over 10000 time steps. Save the results into NumPy arrays.
- Plot the results for each prognostic variable with Matplotlib.
- Plot the results in 3D, make a movie.
- Save your code and results on GitHub.

### Task: impact of numerical precision
- Try to increase or decrease the time step.
- Try to restart the model after 5000 steps.
- Try to restart the model after 5000 steps, but truncating the result of the 5000th step.
