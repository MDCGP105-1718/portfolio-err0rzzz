using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LinkedList
{
          public class LinkedList
        {
            public class Node
            {
                public object Content;
                public Node Next;
            }

            private Node head;

            public LinkedList()
            {
                head = null;
            }

            public InsertBeginning()

            {
                // checks if the head is null, if it is then we know there isn't a beginning
                if (head == null)
                {

                }

                // then creates self and first node's content
                // then sets head to be a pointer to first node

            }

            public InsertAfter(node)

            {
                // takes a node as input argument, checks if there is already a node after
                // then creates a new node, updates pointer in input node and adds a pointer to next node

            }

            public RemoveBeginning()
            {

                // checkes if the head is null, if it isn't delete the first object and updates the head to be the target to which that object had pointed


            }

            public RemoveAfter(node)

            {
                // goes to the destination pointed by input argument, checks if it has content, if it does delete that content 
                // then move its pointer to overwrite the pointer in the argument node

            }

            public length()

            {
                // iterates through the list incrimenting an int for each item
                // then return this int

            }
        }


    }
