# Trello Clone

- [Trello Clone](#trello-clone)
  - [General Idea](#general-idea)
    - [Example image](#example-image)
  - [References](#references)
  - [Functionalities](#functionalities)
  - [Tools](#tools)

## General Idea

Create an application allow login user manages the board by creating, updating and deleting board. Each board has zero or many list inside the board. Each list contains zero or many cards. Each card has name, allow options to be added like due date, check list, add member and priority. Card also allow user to chat and attach file (images, file support)

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
  -  Create a board
  -  Update board information
  -  Delete board
  -  View all the created board and user tagged board
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
  - TODO later
    - Add priority to the card
    - Add animation to the card
- ### Notification
  - When someone add to board ?
  - When someone memtion in the card
  - Any update to the watching card
- ### Chat (maybe)


## Tools
- [Visual studio scode](https://code.visualstudio.com/)
- Postgres version ?
- ....
  
  - ### Visual studio code extension
    - ...
  - ### Markdown extension
    - [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)
