import click

@click.group()
def cli():
  """
  Welcome SIMSSA :D
  """

@cli.command("speak", help="Just print a message.")
@click.argument("message")
def speak(message):
  """
  This is the new hotness.
  """
  print(message)

@cli.command("itest", short_help="Run integration tests.")
def itest():
  import subprocess
  subprocess.call(["bash", "-c", "cd /Users/alex/Documents/GitHub/UTE/python_example && pytest"])
  print("finished?")

@cli.command("rtest", short_help="Run regression tests.")
@click.argument("pypi_repo")
def rtest(pypi_repo):
  import requests
  import subprocess
  from lxml import html

  # Grab all the release versions from pypi.
  url = f"https://pypi.org/project/{pypi_repo}/#history"
  page = requests.get(url)
  tree = html.fromstring(page.content)
  # Ugly string cleaning
  release_list = [x.replace(" ","").replace("\n", "") for x in tree.xpath("//p[@class='release__version']/text()")]
  release_list = [x for x in release_list if x != ""]

  versions = []
  for item in release_list:
    if int(item[0]) < 2:
      release_list.remove(item)
    elif int(item[0]) < 3 and int(item[2]) < 6:
      release_list.remove(item)
    elif (
      int(item[0]) < 3
      and int(item[2]) <= 6
      and int(item[4]) == 0
    ):
      release_list.remove(item)
    else:
      versions.append(item)

  success = []
  failure = []
  for v in reversed(versions):
    try:
      subprocess.run(f"pip install {pypi_repo}=={v}", shell=True, check=True)
      subprocess.run("python -m pytest", shell=True, check=True)
      success.append(v)
    except subprocess.CalledProcessError:
      failure.append(v)

  print(f"Non-Working versions: {failure}")
  print(f"Working versions: {success}")
