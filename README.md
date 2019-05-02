# UTE
__U__nittest __T__raining __E__xamples

There are commonly 3 types of unit tests, and they each seek to answer different questions.

#### Regression testing
  - If I update my dependencies, does my application still work?
  - If I update my OS, does my application still work?

#### Integration testing
  - If I change this base class, will it break all the classes that inherit from it?
  - Make it difficult for typos and other codebreaking faults to get pushed to a version control system. Making sure functions, methods, classes, etc. always accept, execute and return what is expected of them.

#### Acceptance testing
  - Do these features follow the vision of the project?
  - Are these features worth the time required to implement in this project?
