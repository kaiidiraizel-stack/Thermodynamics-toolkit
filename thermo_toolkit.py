import numpy as np
import matplotlib.pyplot as plt

def get_input(prompt, default):
    """Helper function to handle user input with defaults."""
    user_val = input(f"{prompt} [Default {default}]: ")
    return type(default)(user_val) if user_val.strip() != "" else default

def run_heat_diffusion():
    print("\n--- 2D Heat Diffusion Settings ---")
    t_hot = get_input("Enter Top Edge Temperature (°C)", 100.0)
    t_cold = get_input("Enter Bottom Edge Temperature (°C)", 0.0)
    alpha = get_input("Enter Thermal Diffusivity (Alpha)", 2.0)
    grid_size = get_input("Enter Grid Size (e.g., 50 for 50x50)", 50)

   
    dx = 1.0                
    dt = (dx**2) / (4 * alpha) * 0.9  # Stability Governor 
    n_steps = 1000          

    u = np.zeros((grid_size, grid_size))
    u[0, :] = t_hot         
    u[-1, :] = t_cold       
    u[:, 0] = (t_hot + t_cold) / 2  
    u[:, -1] = (t_hot + t_cold) / 2

    gamma = (alpha * dt) / (dx**2)

    print(f"Simulating... (Stability-safe dt calculated at: {dt:.4f})")
    for _ in range(n_steps):
        u[1:-1, 1:-1] = u[1:-1, 1:-1] + gamma * (
            u[2:, 1:-1] + u[:-2, 1:-1] + u[1:-1, 2:] + u[1:-1, :-2] - 4 * u[1:-1, 1:-1]
        )

    plt.figure(figsize=(7, 5))
    plt.imshow(u, cmap='magma', origin='lower', vmin=min(t_hot, t_cold), vmax=max(t_hot, t_cold))
    plt.colorbar(label='Temperature (°C)')
    plt.title(f"Steady State: {t_hot}°C to {t_cold}°C")
    plt.axis('off')
    plt.show()

def run_entropy_sim():
    print("\n--- Entropy Particle Settings ---")
    n_particles = get_input("Number of Particles", 200)
    randomness = get_input("Diffusion Strength (Randomness)", 1.5)
    n_steps = get_input("Number of Time Steps", 500)
    
    box_size = 100
    # Start all particles on the left
    x = np.random.uniform(0, 10, n_particles) 
    y = np.random.uniform(0, box_size, n_particles)
    entropy_values = []

    print("Calculating Microstates...")
    for _ in range(n_steps):
        x += np.random.normal(0, randomness, n_particles)
        y += np.random.normal(0, randomness, n_particles)
        
        x = np.clip(x, 0, box_size)
        y = np.clip(y, 0, box_size)
        
        n_left = np.sum(x < box_size/2)
        p_l = max(n_left / n_particles, 1e-9)
        p_r = max((n_particles - n_left) / n_particles, 1e-9)
        s = -(p_l * np.log(p_l) + p_r * np.log(p_r))
        entropy_values.append(s)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    ax1.scatter(x, y, s=10, color='darkblue', alpha=0.5)
    ax1.axvline(box_size/2, color='red', linestyle='--', label='Divider')
    ax1.set_title(f"Final State ({n_particles} particles)")
    ax1.legend()
    
    ax2.plot(entropy_values, color='green', linewidth=2)
    ax2.set_title("Entropy Curve (S)")
    ax2.set_xlabel("Time (t)")
    ax2.set_ylabel("Disorder (S)")
    plt.tight_layout()
    plt.show()

# interface
if __name__ == "__main__":
    while True:
        print("\n====================================")
        print("    THERMODYNAMICS PYTHON TOOLKIT   ")
        print("====================================")
        print("1. Heat Conduction (Fourier's Law)")
        print("2. Entropy Expansion (Boltzmann/Shannon)")
        print("3. Exit")
        
        user_choice = input("\nChoose a simulation: ")
        
        if user_choice == '1':
            run_heat_diffusion()
        elif user_choice == '2':
            run_entropy_sim()
        elif user_choice == '3':
            print("Shutting down toolkit. Goodbye!")
            break
        else:
            print("Error: Please select 1, 2, or 3.")
