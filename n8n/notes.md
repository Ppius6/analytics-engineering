# n8n

## Introduction

n8n is a workflow automation tool that lets us connect apps and services, move and transform data, automate processes, and write code only when needed.

### Characteristics

It is;
- Node-based
- Event-driven or schedueled
- Self-hostable
- Low-code, not no-code
- Javascript support inside workflows

### When to use n8n

We use n8n when we need
- Complex logic (loops, conditions, branching)
- Data Transformation
- API-heavy workflows
- Cost control
- Data ownership

## Core Mental Model

### Workflow

A workflow can be defined as a `directed graph`, `nodes execute from left to right`, and `data flows between nodes`.

### Node

A node is:
- One action
- One trigger
- One transformation

Examples include `receive webhook`, `fetch data from API`, `filter items`, and `send email`

### Item (Data Unit)

n8n processes data as items

An item looks like

```json
{
  "name": "Mwenda",
  "email": "mpius@erzi.me"
}
```

A `key rule` is that most nodes process items one-by-one.

### Execution

Each workflow run is an execution: 

- Trigger fires
- Nodes execute in order
- Data changes at each step

## Installing n8n

We can run n8n in three main ways:

### n8n Cloud

- Fastest to start
- Monthly cost
- Limited control

### Desktop App

- Local testing
- Not production ready

### Self-Hosted

- Docker
- Full control
- Production-ready

## n8n Interface Overview

An overview of the n8n interface can be as shown below:

![n8n Interface](images/n8n-workflow.webp)

### Sections

The main sections are:

- Canvas where workflows are built
- Nodes panel where all available nodes are
- Node settings panel
- Execution panel to inspect data
- Credentials manager

### Canvas Rules

- Nodes execute left → right
- Multiple branches are allowed
- We can disable nodes
- We can test nodes individually

## Data Flow & Expressions

### Data Passing

Each node receives: 

```
Input items → processes → outputs items
```

### Expressions

Expressions let us reference data dynamically. The syntax is as shown below:

```
{{ $json.fieldName }}
```

An example is:

```
{{ $json.email }}
```

### Common Expression Helpers

- `$json` - current item
- `$node["Node Name"].json`
- `$now`
- `$execution.id`

### Mapping Fields

We can:
- Drag fields from execution panel
- Write expressions manually
- Combine text + expressions

## Core Control Nodes

### Set Node

It helps `create`, `rename`, and `remove fields`. We can use it to `clean data`, and `prepare payloads`

### IF Node

It's purpose is `conditional branching`. 

Exxamples include;
- If email exists
- If status == "paid"
- If amount > 100

It produces:

- True branch
- False branch

### Merge Node

It's purpose is to `combine data from multiple branches`

Its models include:

- `Append`
- `Merge by key`
- `Pass-through`

### Split In Batches

Its purpose it to loop over large datasets and control rate limits

