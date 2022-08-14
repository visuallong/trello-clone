# Trello Clone

- [Trello Clone](#trello-clone)
  - [General Idea](#general-idea)
    - [Example image](#example-image)
  - [References](#references)
  - [Functionalities](#functionalities)
  - [Requirements](#requirements)
  - [Development tools](#development-tools)
  - [Web UI requirements](#web-ui-requirements)
    - [Web component](#web-component)

## General Idea

Create an application allow login user manages the board by creating, updating and deleting board. Each board has zero or many list inside the board. Each list contains zero or many cards. Each card has name, allow options to be added like due date, check list, add member and priority. Card also allow user to chat and attach file (images, file support)

See what is [Kanban](https://www.ntaskmanager.com/blog/what-is-kanban/)

### Example image

Trello home page example 1

![](https://getnave.com/blog/wp-content/uploads/2018/03/how-trello-and-kanban-work-together.png "Trello home page")

Trello Home page example 2

![](https://embedwistia-a.akamaihd.net/deliveries/adfdcfdf4892a13efabb20056dddbed1.webp?image_crop_resized=1280x720 "Trello home page 2")

Trello card details

![](https://blog-cdn.everhour.com/blog/wp-content/uploads/2019/11/This_is_a_card__Drag_it_to_the__Tried_It__List_to_show_it_s_done__%E2%86%92_on__Tutorial_Board___Trello.png "Trello card detail")

## References

- https://getnave.com/blog/trello-kanban-boards/

## Functionalities

- ### User
  - Create an account
  - Login
- ### Board
  - Create a board
  - Update board information
  - Delete board
  - View all the created board and user tagged board
- ### List
  - Create a list inside a board
  - Update list information
  - Delete list (TODO: should delete or not?)
  - View all cards in that list (TODO: include search or not ?, which functionality should be added)
- ### Card
  - Create a card
  - Update a card info
  - Add options to the card
    - Add due date
    - Checklist
    - Tag member
    - Attach file
  - Delete a card
  - Allow user to move the card from one list to another
- ### Notification
  - When someone add to board ?
  - When someone memtion in the card
  - Any update to the watching card
- ### Next feature
  - Add priority to the card
  - Add animation to the card
  - Chat

## Requirements

- [Python 3.10](https://www.python.org/downloads/)
- [Postgres 11 or greater](https://www.postgresql.org/download/)
- [React](https://reactjs.org/tutorial/tutorial.html#setup-option-2-local-development-environment)

## Development tools

- [Visual studio code](https://code.visualstudio.com/)
  - Visual studio code extension
    - [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)
    - [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
    - [Docker](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker)
- [Docker](https://www.docker.com/get-started/)
- [Fastapi](https://fastapi.tiangolo.com/)

## Web UI requirements

1. Login page
2. Register page
3. Home page (see all the current board)
4. Create board modal
5. View board list page
6. Add a new list modal
7. Create card modal (for list)
8. Can drag one card from the list to another
9. Click the card to see the details

### Web component

- Input component [@Long](https://github.com/visuallong)
- Form component [@Nguyen](https://github.com/BabyfaceDeveloper)
- Card component [@Long](https://github.com/visuallong)
- List component [@Nguyen](https://github.com/BabyfaceDeveloper)
- Board component [@Long](https://github.com/visuallong)
- Modal component [@Nguyen](https://github.com/BabyfaceDeveloper)
