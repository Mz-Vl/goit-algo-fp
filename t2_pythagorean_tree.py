import turtle


def draw_pifagor_tree(branch_length, t, angle, recursion_level):
    if recursion_level == 0:
        return
    else:
        # main branch
        t.forward(branch_length)
        t.right(angle)

        # right subtree
        draw_pifagor_tree(0.7 * branch_length, t, angle, recursion_level - 1)

        # Move back to the original position
        t.left(2 * angle)

        # left subtree
        draw_pifagor_tree(0.7 * branch_length, t, angle, recursion_level - 1)

        # Move back to the original position
        t.right(angle)
        t.backward(branch_length)


def main():
    # Setup turtle
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(2)
    t.color("brown")

    # Get user input for recursion level
    recursion_level = int(input("Enter recursion level for the Pythagorean tree: "))

    # Set initial parameters and draw the tree
    branch_length = 100
    angle = 45
    t.left(90)
    draw_pifagor_tree(branch_length, t, angle, recursion_level)

    # Close the window on click
    window.exitonclick()


if __name__ == "__main__":
    main()
