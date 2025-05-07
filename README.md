# Stock-SpaceOptimizer
Software to optimize warehouse inventory management, maximizing space usage, calculating optimal stock levels, and enhancing distribution. Outputs digital layouts for efficient item placement.

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Architecture](#architecture)
4. [Setup Instructions](#setup-instructions)
5. [Usage Guidelines](#usage-guidelines)
6. [Codebase Structure](#codebase-structure)
7. [System Requirements](#system-requirements)
8. [Troubleshooting](#troubleshooting)
9. [Contribution Guidelines](#contribution-guidelines)
10. [License](#license)

## Overview
**Warehouse-StockOrganizer** is a sophisticated Python-based software solution designed to optimize inventory management and space utilization in urban warehouse environments. The system processes inventory data from a CSV file, employs an advanced bin-packing algorithm to maximize storage efficiency, and generates a digital layout for precise product placement. Supporting dry, refrigerated, and frozen storage zones, it features a 3D visualization module powered by Pygame and OpenGL to simulate warehouse layouts and operative navigation. Outputs include a `salida.csv` file detailing product assignments and a `FotosRacks` folder containing frontal and lateral images for each rack, illustrating product placements and quantities, enabling efficient inventory retrieval and streamlined operations.

Designed for a central warehouse measuring 8.18m (width) x 8.5m (length) x 2.90m (height), with 69.53m² of floor space and 201.64m³ of storage volume, the system addresses inefficiencies in space organization, stock quantity optimization, and storage congestion, offering a scalable, data-driven solution for modern logistics challenges.

## Features
- **Space Optimization**: Utilizes a bin-packing algorithm (`binPackingV3.py`) to arrange products in racks, minimizing unused space while adhering to dimensional constraints of dry, refrigerated, and frozen zones.
- **Inventory Management**: Analyzes input CSV data to compute optimal stock quantities based on maximum capacity and storage conditions, enhancing resource allocation.
- **3D Visualization**: Renders a real-time 3D warehouse model (`Simulacion.py`) using Pygame and OpenGL, displaying racks, products, refrigeration chambers, and operative paths.
- **Multi-Zone Support**:
  - **Dry Zone**: Vertical racks optimized for high-rotation products.
  - **Refrigerated Zone**: Racks designed for temperature-controlled storage.
  - **Frozen Zone**: Equipment for low-temperature frozen goods.
- **Output Generation**:
  - `salida.csv`: Details products, quantities, and assigned racks (e.g., `S1`, `R2`, `C3`).
  - `FotosRacks` folder: Contains two images per rack (frontal and lateral views), visualizing product placements and quantities within each rack.
- **Operative Navigation**: Simulates warehouse operatives (`Persona.py`) navigating predefined nodes, ensuring efficient pathfinding and workflow.
- **Configurability**: Supports customizable rack dimensions via command-line arguments and warehouse settings via `Settings.yaml`.

## Architecture
The system is developed using Python 3.8+ and integrates multiple libraries for data processing, visualization, and optimization. Its modular architecture ensures maintainability and scalability:

- **`main.py`**: Entry point, parsing command-line arguments with `argparse` to configure simulation parameters, including input CSV, rack dimensions, and output settings. Logs execution milestones with colored output.
- **`Simulacion.py`**: Manages 3D visualization, initializing Pygame and OpenGL, rendering the warehouse (floor, walls, racks, refrigeration chambers), and simulating operative movement. Generates `FotosRacks` images.
- **`preparaDatos.py`**: Processes input CSV data with `pandas`, sorts products by height, and assigns them to racks/zones using the bin-packing algorithm. Configures storage zones.
- **`binPackingV3.py`**: Implements a 3D bin-packing algorithm, optimizing product placement with rotation support. Assigns colors for visualization and generates output data.
- **`ZonaRack.py`**: Defines the `ZonaRack` class, managing rack placement and rendering within zones.
- **`Persona.py`**: Models operatives with graph-based pathfinding across nodes defined in `data.py`.
- **`data.py`**: Specifies warehouse obstacles, navigation nodes, and adjacency matrices for pathfinding. Loads `Settings.yaml` with `pyyaml`.
- **`Settings.yaml`**: Configures warehouse dimensions, visualization parameters, and operative settings.

## Setup Instructions
To deploy the Warehouse-StockOrganizer project, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/Warehouse-StockOrganizer.git
   cd Warehouse-StockOrganizer
   ```

2. **Install Python**:
   Verify Python 3.8 or higher is installed:
   ```bash
   python --version
   ```

3. **Install Dependencies**:
   No `requirements.txt` is provided. Install required libraries manually:
   ```bash
   pip install pygame pyopengl pandas numpy pyyaml
   ```
   **Dependencies**:
   - `pygame`: Renders 3D visualizations and generates rack layout images.
   - `pyopengl`: Enables OpenGL for 3D rendering.
   - `pandas`: Processes CSV data.
   - `numpy`: Performs numerical computations.
   - `pyyaml`: Parses `Settings.yaml`.

4. **Configure Settings**:
   The provided `Settings.yaml` defines warehouse and visualization parameters:
   - **Warehouse Dimensions**:
     - `DimX: 900` (9m, adjusted from 8.18m).
     - `DimY: 260` (2.6m, adjusted from 2.90m).
     - `DimZ: 950` (9.5m, adjusted from 8.5m).
   - **Visualization Parameters**:
     - `screen_width: 500`, `screen_height: 500`: Window resolution.
     - `FOVY: 80`, `ZNEAR: 0.01`, `ZFAR: 1800.0`: Camera settings.
     - `EYE_X: 601`, `EYE_Y: 1000`, `EYE_Z: 601`: Camera position.
     - `CENTER_X: 500`, `CENTER_Y: 0`, `CENTER_Z: 500`: Camera focus.
   - **Operative Settings**:
     - `Agentes: 10`: Number of simulated operatives.
   - **Materials**:
     - `Materials: ./Materials/`: Directory for texture files.
   Modify `Settings.yaml` to align with specific warehouse or visualization needs.

5. **Prepare Input Data**:
   Create a CSV file with the following columns:
   - `DESCRIPCIÓN COMPLETA`: Product name (string).
   - `Largo`, `Ancho`, `Altura`: Dimensions (cm, numeric).
   - `C. Maximo`: Maximum stock quantity (string, e.g., "1,000").
   - `Condición`: Storage condition (`S` for dry, `R` for refrigerated, `C` for frozen).
   Example:
   ```
   DESCRIPCIÓN COMPLETA,Largo,Ancho,Altura,C. Maximo,Condición
   Pizza Dough,30,20,10,1000,S
   Cheese,25,15,8,500,R
   Pepperoni,20,10,5,300,C
   ```

6. **Create Materials Directory**:
   Ensure the `./Materials/` directory exists with texture images (e.g., PNG or JPEG). If textures are not used, create an empty `./Materials/` directory.

## Usage Guidelines
Run the simulation using the main script with command-line arguments. Below is a comprehensive guide:

1. **Command Syntax**:
   ```bash
   python main.py RETO --CSV input.csv --vRackC "100,50,200,5" --vRackR "100,50,200,5" --vRackS "100,50,200,5" --confianza 10 --salida output.csv
   ```

   **Arguments**:
   - `--CSV`: Path to input CSV (required).
   - `--vRackC`: Frozen rack dimensions (format: `length,width,height,spaces` in cm, required).
   - `--vRackR`: Refrigerated rack dimensions (same format, required).
   - `--vRackS`: Dry rack dimensions (same format, required).
   - `--confianza`: Confidence percentage for stock calculations (optional, default: 10).
   - `--salida`: Output CSV file name (optional, default: `salida.csv`).

   **Example**:
   ```bash
   python main.py RETO --CSV products.csv --vRackC "100,50,200,5" --vRackR "100,50,200,5" --vRackS "100,50,200,5" --salida warehouse_output.csv
   ```

2. **Execution Flow**:
   - **Input Processing** (`preparaDatos.py`):
     - Reads CSV using `pandas`, converting dimensions to floats.
     - Sorts products by height (descending) for stacking efficiency.
     - Splits products by `Condición` (`S`, `R`, `C`), adjusting quantities (`C. Maximo` divided by 4, rounded up).
   - **Bin-Packing** (`binPackingV3.py`):
     - Assigns products to racks, respecting dimensions and conditions.
     - Rotates products (length/width or length/height) to optimize space.
     - Assigns unique colors for visualization.
     - Generates data for `salida.csv` and `FotosRacks` images.
   - **Zone Configuration** (`preparaDatos.py`):
     - Creates `ZonaRack` instances for dry, refrigerated, and frozen zones.
     - Positions zones to avoid conflicts with warehouse constraints.
   - **Visualization** (`Simulacion.py`):
     - Initializes Pygame and OpenGL per `Settings.yaml`.
     - Renders:
       - Floor, walls, and obstacles from `data.py`.
       - Refrigeration chambers (`refrigerador`).
       - Racks (dry: gray `[0.4,0.4,0.4]`, refrigerated: light blue `[0,0.5,1]`, frozen: blue `[0,0,1]`).
       - Products as colored cubes.
       - Operatives as cuboids navigating nodes.
     - Captures frontal and lateral images for each rack in `FotosRacks`.
   - **Output**:
     - `salida.csv`: Product assignments (e.g., `"Pizza Dough",500,S1`).
     - `FotosRacks/`: Two images per rack (e.g., `S1_frontal.png`, `S1_lateral.png`) showing products and quantities.

3. **Visualization Controls**:
   - Displays the warehouse in real-time.
   - Close the Pygame window to terminate the simulation.
   - Camera is fixed at `[601,1000,601]`, focusing on `[500,0,500]` (`Settings.yaml`).
     

4. **Output Details**:
   - **salida.csv**:
     ```
     Producto,Cantidad,Rack
     "Pizza Dough",500,S1
     "Cheese",200,R1
     "Pepperoni",150,C1
     ```
 ## FotosRacks

  Images generated from 3D renderings showcasing the rack structure, product positions, and quantities.

- **Images**:
  - ![Rack Structure 1](https://github.com/user-attachments/assets/64a2076e-f1be-47cd-b583-91b7dbeb09e4)
  - ![Rack Structure 2](https://github.com/user-attachments/assets/42987aa2-aaaf-4413-9a65-42e944a85abc)

## Codebase Structure
The codebase is organized for clarity and extensibility:

- **`main.py`**:
  - Parses `RETO` subcommand arguments with `argparse`.
  - Validates inputs and logs execution with green-colored output.
  - Invokes `Simulacion.Simulacion`.

- **`Simulacion.py`**:
  - Initializes Pygame (500x500 window) and OpenGL (double buffering).
  - Configures perspective (`gluPerspective`) and camera (`gluLookAt`) per `Settings.yaml`.
  - Loads textures from `./Materials/` (`Texturas`).
  - Renders warehouse components:
    - `plano`: Floor, walls, nodes, and links.
    - `refrigerador`: Transparent refrigeration chamber.
    - `obstaculos`: Columns and doors from `data.py`.
    - Racks/products via `ZonaRack.draw`.
    - Operatives via `Persona.draw`.
  - Captures frontal and lateral images for each rack in `FotosRacks`.
  - Runs simulation loop (10ms updates).

- **`preparaDatos.py`**:
  - Reads CSV, converting `Altura` to floats (non-numeric set to 0).
  - Sorts products by height for stacking.
  - Splits products by `Condición`, adjusting quantities.
  - Calls `binPacking` per zone with rack dimensions.
  - Configures zones:
    - Dry: Multiple `ZonaRack` at fixed positions (e.g., `[500,5,150]`).
    - Refrigerated/Frozen: Dynamic positioning from `DimX-720-98`.
  - Returns zone lists and refrigeration chamber position.

- **`binPackingV3.py`**:
  - Executes 3D bin-packing with rotation support.
  - Assigns grid-based random colors for visualization.
  - Optimizes placement:
    - Computes products per level (`dimX*dimY`).
    - Stacks vertically up to rack height/spaces.
    - Manages partial rows/columns.
  - Generates `salida.csv` and `FotosRacks` data.
  - Tracks products in `productosAlmacenados`.

- **`ZonaRack.py`**:
  - Defines `ZonaRack` class for zone/rack management.
  - Places racks (`agregarRack`) with spacing (`distancia`).
  - Renders zones as quads and racks via `Rack.draw`.

- **`Persona.py`**:
  - Models operatives as 50x160x50 cm cuboids.
  - Implements pathfinding:
    - Uses `data.py` nodes and adjacency matrix.
    - Selects random nodes (`defineObjetivo`) and paths (`defineRuta`).
    - Moves at 150 cm/s (`dTiempo: 0.01s`).
  - Renders with brown color (`[0.5,0.1,0]`).

- **`data.py`**:
  - Defines obstacles as 3D quads (columns, walls, doors).
  - Provides 13 navigation nodes (e.g., `[900,0,280]`) and 13x13 adjacency matrix.
  - Loads `Settings.yaml` into `Settings` class.

- **`Settings.yaml`**:
  - Specifies warehouse (9m x 2.6m x 9.5m), visualization (500x500, 80° FOV), camera, 10 operatives, and `./Materials/` directory.

## System Requirements
- **Operating System**: Windows, macOS, or Linux.
- **Python**: 3.8 or higher.
- **Hardware**:
  - CPU: 2 GHz or faster (multi-core preferred).
  - RAM: 4 GB minimum (8 GB recommended).
  - GPU: OpenGL-compatible for rendering and image generation.
- **Storage**: 500 MB for code, dependencies, and outputs.

## Troubleshooting
- **Missing `./Materials/`**: Create the directory with PNG/JPEG files or leave empty.
- **CSV Errors**: Verify columns and numeric `Largo`, `Ancho`, `Altura`.
- **Visualization Issues**: Update OpenGL drivers and validate `Settings.yaml`.
- **Rack Dimension Errors**: Use `length,width,height,spaces` format for `--vRack` arguments.
- **Missing `FotosRacks` Images**: Confirm Pygame installation and folder write permissions.

## Contribution Guidelines
Contributions are encouraged to enhance Warehouse-StockOrganizer. To contribute:

1. **Fork the Repository**:
   ```bash
   git clone https://github.com/your-username/Warehouse-StockOrganizer.git
   ```
2. **Create a Feature Branch**:
   ```bash
   git checkout -b feature/YourFeature
   ```
3. **Commit Changes**:
   Adhere to PEP 8 with descriptive messages:
   ```bash
   git commit -m "Add YourFeature: Detailed description"
   ```
4. **Push to GitHub**:
   ```bash
   git push origin feature/YourFeature
   ```
5. **Submit a Pull Request**:
   Include a detailed description of changes, impact, and tests.

**Guidelines**:
- Follow PEP 8 standards.
- Include unit tests (e.g., `pytest`).
- Update documentation (README, comments).
- Ensure Python 3.8+ compatibility.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
