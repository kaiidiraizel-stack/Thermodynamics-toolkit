# Thermodynamics Python Toolkit 🌡️

A versatile computational physics suite designed to simulate and visualize fundamental thermodynamic principles. This toolkit allows users to explore heat conduction through solids and the statistical nature of entropy increase in gas expansion.

---

## 🚀 Features

### 1. 2D Heat Diffusion (Macroscopic)
Models how thermal energy moves through a solid material using **Fourier's Law of Conduction**.
* **Physics:** Solves the 2D Heat Equation using the Finite Difference Method.
* **Interactive:** User-defined temperatures and material properties (Thermal Diffusivity).
* **Stability:** Features an automatic **Stability Governor** that calculates the maximum safe time-step ($\Delta t$) to prevent numerical divergence.

### 2. Entropy & Particle Diffusion (Microscopic)
Demonstrates the **Second Law of Thermodynamics** and the statistical transition from order to chaos.
* **Physics:** Uses a "Particle in a Box" random-walk model.
* **Math:** Calculates **Shannon Entropy** ($S = -\sum p_i \ln p_i$) in real-time.
* **Insight:** Visualizes how systems naturally move toward higher-probability microstates (equilibrium).

---

## 🛠️ Installation

Ensure you have Python 3.x installed. You will need `NumPy` for the matrix calculations and `Matplotlib` for the visualizations.

```bash
pip install numpy matplotlib
```

---

## 📖 How to Use

1.  **Run the Script:**
    ```bash
    python thermodynamics_toolkit.py
    ```
2.  **Navigate the Menu:**
    * **Option 1:** Explore heat flow. Enter the temperatures for the top and bottom edges of a plate. Adjust "Alpha" to simulate different materials (e.g., Copper vs. Glass).
    * **Option 2:** Explore entropy. Change the particle count and "Randomness" (representing temperature/kinetic energy) to see how quickly disorder increases.
3.  **Defaults:** Press **Enter** on any input prompt to use the pre-configured optimal settings.

---

## 🧬 Underlying Theory

### The Heat Equation
The movement of heat is calculated by looking at the "curvature" of temperature at every point on a grid:
$$\frac{\partial u}{\partial t} = \alpha \left( \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} \right)$$

### The Entropy Formula
Entropy is calculated based on the probability ($p$) of particles being in a specific region of the box. As particles spread from the left to the right, the probability distribution becomes more uniform, causing $S$ to rise:
$$S = -k_B \sum p_i \ln p_i$$

---

## 📂 Project Structure

* `get_input()`: A robust helper function that handles user interactions and provides defaults.
* `run_heat_diffusion()`: Contains the vectorized NumPy logic for thermal conduction.
* `run_entropy_sim()`: Manages the random-walk simulation and statistical calculations.
* **Stability Governor:** Logic that enforces $\Delta t \leq \frac{\Delta x^2}{4\alpha}$ to ensure the simulation remains physically accurate.

