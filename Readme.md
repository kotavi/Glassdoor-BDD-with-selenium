# Python / Behave / Cucumber


`python3 -m pip install behave`

### Notes
- After *.feature file is created PyCharm will sugest to install Gherkin plugin
- You'll get error 'ConfigError: No steps directory in <your_path>/features' if 'steps' folder was not created
- 

### To execute tests

`
behave features/loginToJenkins.feature
`

`
behave features/loginToJenkins.feature --no-color
`

* To run all .feature files

`behave --format=plain --show-timings`



## Assertion Matcher Library

`python3 -m pip install pytest-bdd`

or

`python3 -m pip install nose`


### Useful links

- https://the-creative-tester.github.io/Python-Web-Browser-Automation-Behave/

### Examples of XPATHs

#### Link:

   `//a[text()='Features']`
   
   `//a[contains(text(), 'Features')]`

#### Button

`//button[@class='class1 class2 class3 ....']`

`//button[@class='class1' and @type='Submit']`

`//button[contains(text(), 'Submit')]`

#### Table
