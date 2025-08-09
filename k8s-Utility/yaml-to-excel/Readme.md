# Python yaml2excel script

**Author :** Kaustav Das  
**Created:** 8/9/2025 04:18 PM  
**Last Updated:** 8/9/2025 04:18 PM  



## Prerequisites
- Python 3.9+ (recommended)
- [Anaconda](https://www.anaconda.com/download) or Miniconda installed

---

## Environment Setup

1. **Activate your Conda environment**
   ```bash
   conda activate <project-path>\k8s_util
   ```

2.  **Verify active environment**
    ```bash
    conda env list
    ```
    Example output:
    ```bash
      *   E:\GitHub\k8s-Utility\yaml-to-excel\k8s_util
          E:\GitHub\Python-Dev\GenAI-Python\PythonCode\venv
    base  E:\LearningSoftware\Python\Anaconda3
    ```
    ** Make sure right enviroment is selected **

3.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

* * *

## Project Structure
-----------------

```
yaml-to-excel/
├── src/
│   └── yaml2excel.py         # Main script
├── test/
│   └── complex_values.yml    # Example test YAML file
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

* * *

Usage
-----

### Basic Command

```bash
python src/yaml2excel.py ./test/complex_values.yml complex_dev_values.xls
```

* * *
#### Example Input YAML
------------------

```yaml
global:
  app:
    name: myapp
    version: 1.2.3
service:
  port: 8080
servers:
  - name: server1
    ip: 10.0.0.1
```

#### Example Output Excel
--------------------

| Key | Value |
| --- | --- |
| global.app.name | myapp |
| global.app.version | 1.2.3 |
| service.port | 8080 |
| servers\[0\].name | server1 |
| servers\[0\].ip | 10.0.0.1 |

* * *