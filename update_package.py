import pkg_resources

def get_current_version(package_name):
    try:
        distribution = pkg_resources.get_distribution(package_name)
        return distribution.version
    except pkg_resources.DistributionNotFound:
        # Xử lý trường hợp khi gói chưa được cài đặt
        return None

# Sử dụng hàm để lấy phiên bản hiện tại của gói
#current_version = get_current_version("RStockvn")


import requests
import click

def get_latest_version(package_name):
    try:
        response = requests.get(f"https://pypi.org/pypi/{package_name}/json")
        data = response.json()
        return data["info"]["version"]
    except Exception as e:
        print(f"Không thể lấy phiên bản mới: {str(e)}")
        return None

def check_for_updates():
    current_version = get_current_version("RStockvn")
    latest_version = get_latest_version("RStockvn")

    if latest_version and latest_version > current_version:
        return f"Có phiên bản mới {latest_version}, vui lòng cập nhật bằng hàm updates_package_RStockvn() hoặc '!pip install --upgrade RStockvn' trong ô code Jupyter"
    elif latest_version and latest_version == current_version:
        return f'Đã là phiên bản mới {latest_version}'



import subprocess
def updates_package_RStockvn():
    latest_version = get_latest_version("RStockvn")
    
    if latest_version:
        # Tạo lệnh cài đặt
        install_command = f'pip install --upgrade RStockvn'
        try:
            # Gọi lệnh từ command prompt hoặc Anaconda Prompt
            subprocess.run(install_command, shell=True, check=True)
            print(f"Cập nhật thành công! Phiên bản mới nhất là {latest_version}")
        except subprocess.CalledProcessError:
            print("Không thể cập nhật package.")
