from distutils.core import setup


setup(
    name="infrastructure_arkea",
    description="Package pour gérer les clusters",
    requires=["PyYAML"],
    packages=["infra"],
    package_dir={"infra": "src/infra"},
)
