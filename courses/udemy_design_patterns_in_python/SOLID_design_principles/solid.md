# SOLID Principle

*Table of contents:*
- [SOLID Principle](#solid-principle)
  - [Single responsibility principle](#single-responsibility-principle)
    - [Good Example](#good-example)
    - [Bad Example](#bad-example)
    - [Fixed the example](#fixed-the-example)
    - [Summary](#summary)

## Single responsibility principle

Single responsibility principle (SRP) also called Separation of concern is a the first principle we are going to learn. 

> `Unix Philosophy`: Write programs that do one thing and do it really well.

The idea is that we design our class to be responsible for one type of work and this work only. You don't need to mix it with others. Let's look at the example with `journal` class. It contains attributes and methods only related with journal.

### Good Example

```python
# Good design
class Journal:
    def __init__(self) -> None:
        self.entries = []
        self.count = 0
    
    def add_entry(self, text):
        self.count += 1
        self.entries.append(f"{self.count}: {text}")
        
    def remove_entry(self, pos):
        del self.entries[pos]
    
    def __str__(self):
        return '\n'.join(self.entries)
    


if __name__ == "__main__":
    j = Journal()
    j.add_entry('I cried today')
    j.add_entry('I ate a bug')
    print(f'Journal entries: \n{j}')    
```

Feel free to play around with it.

### Bad Example

Let's look at a bad example now where you also have the following methods:
- `save()`
- `load()`
- `load_from_web()`

This is bad design for the following reasons,
- Imagine you know have 10 classes, and you implement the problem of persistence (save, load) in all of them. It's redundant work and also once the I/O methods changes, you need to modify on all 10 of them.

底层逻辑是一样的, DRY principle, and make abstraction out of it.

```python
class Journal:
    def __init__(self) -> None:
        self.entries = []
        self.count = 0
    
    def add_entry(self, text):
        self.count += 1
        self.entries.append(f"{self.count}: {text}")
        
    def remove_entry(self, pos):
        del self.entries[pos]
    
    def save(self, filename):
        file = open(filename, 'w')
        file.write(str(self))
        file.close()
    
    def load(self, filename):
        pass
    
    def load_from_web(self, uri):
        pass
    
    def __str__(self):
        return '\n'.join(self.entries)

if __name__ == "__main__":
    j = Journal()
    j.add_entry('I cried today')
    j.add_entry('I ate a bug')
    print(f'Journal entries: \n{j}') 
```

### Fixed the example

How, we need to fix the bad design in the last section. All we need to do is to separate our concerns of persistence to another class to take care of it.

> Concept of persistence is first visited when i picked up `docker`. Persistence with volume. Although container is designed to be ephemeral 
> but volume (data) shall be consistence.


```python
class Journal:
    def __init__(self) -> None:
        self.entries = []
        self.count = 0
    
    def add_entry(self, text):
        self.count += 1
        self.entries.append(f"{self.count}: {text}")
        
    def remove_entry(self, pos):
        del self.entries[pos]
    
    
    def __str__(self):
        return '\n'.join(self.entries)
    
class PersistenceManager():
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, "w")
        file.write(str(journal))
        file.close()



if __name__ == "__main__":
    j = Journal()
    j.add_entry('I cried today')
    j.add_entry('I ate a bug')
    print(f'Journal entries: \n{j}')
    
    manager = PersistenceManager()
    manager.save_to_file(j,"./test")
```

### Summary
The takehome for the Single responsibility principle is that i am designing a class that does one thing but does one thing really well. Also, we are trying to eliminate as many as god objects.

For those who intersted in learning "god objects". Please read this conference paper for more [details](https://www.researchgate.net/publication/307572331_Identification_of_Web_Service_Refactoring_Opportunities_as_a_Multi-objective_Problem).

![](https://www.researchgate.net/profile/William-Grosky/publication/307572331/figure/fig1/AS:792593864597508@1565980511623/An-example-of-god-object-Web-service.png)