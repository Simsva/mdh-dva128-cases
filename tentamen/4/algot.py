#!/usr/bin/env python3
import os, json

children = '[{"name":"Simon Lund","parents":{"mother":"Britt Lund","father":"Jonathan Lund"}},{"name":"Alexandra Fredriksson","parents":{"mother":"Elin Fredriksson","father":"Arvid Fredriksson"}},{"name":"Frida Eklund","parents":{"mother":"Josefin Eklund","father":"Tommy Eklund"}},{"name":"Bengt Holmgren","parents":{"mother":"Monica Holmgren","father":"Christoffer Holmgren"}},{"name":"Leif Mattsson","parents":{"mother":"Louise Mattsson","father":"Mikael Mattsson"}},{"name":"Anders Ström","parents":{"mother":"Sofia Ström","father":"Bo Ström"}},{"name":"Erik Åberg","parents":{"mother":"Birgitta Åberg","father":"Kenneth Åberg"}},{"name":"Rune Pålsson","parents":{"mother":"Elsa Pålsson","father":"Magnus Pålsson"}},{"name":"Annika Dahlberg","parents":{"mother":"Caroline Dahlberg","father":"Peter Dahlberg"}},{"name":"Martin Fransson","parents":{"mother":"Elisabeth Fransson","father":"Sven Fransson"}},{"name":"Kristin Gustafsson","parents":{"mother":"Frida Gustafsson","father":"Ove Gustafsson"}},{"name":"Helena Berg","parents":{"mother":"Ulrika Berg","father":"Hugo Berg"}},{"name":"William Pålsson","parents":{"mother":"Klara Pålsson","father":"Jan Pålsson"}},{"name":"Jessica Abrahamsson","parents":{"mother":"Viola Abrahamsson","father":"Wilhelm Abrahamsson"}},{"name":"Georg Lindholm","parents":{"mother":"Ulrika Lindholm","father":"Hans Lindholm"}},{"name":"David Nyberg","parents":{"mother":"Kristina Nyberg","father":"Stig Nyberg"}},{"name":"Amanda Abrahamsson","parents":{"mother":"Frida Abrahamsson","father":"Anton Abrahamsson"}},{"name":"Lisbeth Jonasson","parents":{"mother":"Johanna Jonasson","father":"Mats Jonasson"}},{"name":"Felicia Lindberg","parents":{"mother":"Emelie Lindberg","father":"Per Lindberg"}},{"name":"Jonathan Bergström","parents":{"mother":"Ingeborg Bergström","father":"Alf Bergström"}},{"name":"Marcus Pettersson","parents":{"mother":"Viola Pettersson","father":"Gösta Pettersson"}},{"name":"Louise Bergqvist","parents":{"mother":"Viktoria Bergqvist","father":"Emanuel Bergqvist"}},{"name":"Kristin Jonasson","parents":{"mother":"Irene Jonasson","father":"Lennart Jonasson"}},{"name":"Annika Gunnarsson","parents":{"mother":"Anneli Gunnarsson","father":"Kenneth Gunnarsson"}},{"name":"Pia Lindström","parents":{"mother":"Linda Lindström","father":"Magnus Lindström"}},{"name":"Lisbeth Ekström","parents":{"mother":"Anita Ekström","father":"Kenneth Ekström"}},{"name":"Sebastian Ekström","parents":{"mother":"Marie Ekström","father":"Göran Ekström"}},{"name":"Lisbeth Axelsson","parents":{"mother":"Anita Axelsson","father":"Isak Axelsson"}},{"name":"Therese Jonasson","parents":{"mother":"Johanna Jonasson","father":"Mats Jonasson"}},{"name":"Maria Mattsson","parents":{"mother":"Kristin Mattsson","father":"Daniel Mattsson"}},{"name":"Björn Björklund","parents":{"mother":"Ulrika Björklund","father":"Thomas Björklund"}},{"name":"Dan Abrahamsson","parents":{"mother":"Anneli Abrahamsson","father":"Mats Abrahamsson"}},{"name":"Per Jonsson","parents":{"mother":"Isabelle Jonsson","father":"Robert Jonsson"}},{"name":"Peter Abrahamsson","parents":{"mother":"Frida Abrahamsson","father":"Anton Abrahamsson"}},{"name":"Helena Ali","parents":{"mother":"Pia Ali","father":"Lennart Ali"}},{"name":"Wilhelm Lindholm","parents":{"mother":"Jessica Lindholm","father":"Lars Lindholm"}},{"name":"Mikael Mårtensson","parents":{"mother":"Gunilla Mårtensson","father":"Niklas Mårtensson"}},{"name":"Gunilla Björklund","parents":{"mother":"Marianne Björklund","father":"Jan Björklund"}},{"name":"Tommy Axelsson","parents":{"mother":"Maria Axelsson","father":"Karl Axelsson"}},{"name":"Georg Holm","parents":{"mother":"Gun Holm","father":"Johan Holm"}},{"name":"Madeleine Gustafsson","parents":{"mother":"Astrid Gustafsson","father":"Roger Gustafsson"}},{"name":"Julia Björk","parents":{"mother":"Sofia Björk","father":"Marcus Björk"}},{"name":"Alexander Mattsson","parents":{"mother":"Kristin Mattsson","father":"Daniel Mattsson"}},{"name":"Anna Lindström","parents":{"mother":"Elisabeth Lindström","father":"Mattias Lindström"}},{"name":"Isak Johansson","parents":{"mother":"Ann Johansson","father":"Thomas Johansson"}},{"name":"Isabelle Sjöberg","parents":{"mother":"Frida Sjöberg","father":"Rickard Sjöberg"}},{"name":"Barbro Berg","parents":{"mother":"Isabelle Berg","father":"Wilhelm Berg"}},{"name":"Lucas Lindström","parents":{"mother":"Ellinor Lindström","father":"Lennart Lindström"}},{"name":"Helen Åkesson","parents":{"mother":"Matilda Åkesson","father":"John Åkesson"}},{"name":"Elias Bergström","parents":{"mother":"Irene Bergström","father":"Kurt Bergström"}},{"name":"Marie Pålsson","parents":{"mother":"Elsa Pålsson","father":"Magnus Pålsson"}},{"name":"Kjell Henriksson","parents":{"mother":"Ingeborg Henriksson","father":"Mikael Henriksson"}},{"name":"Amanda Sandström","parents":{"mother":"Marianne Sandström","father":"Bo Sandström"}},{"name":"Yvonne Forsberg","parents":{"mother":"Klara Forsberg","father":"Nils Forsberg"}},{"name":"Niklas Håkansson","parents":{"mother":"Margareta Håkansson","father":"Stig Håkansson"}},{"name":"Sofie Nyström","parents":{"mother":"Britt Nyström","father":"Arvid Nyström"}},{"name":"Charlotte Ström","parents":{"mother":"Linda Ström","father":"Emanuel Ström"}},{"name":"Helen Arvidsson","parents":{"mother":"Rebecca Arvidsson","father":"Jakob Arvidsson"}},{"name":"Kent Lind","parents":{"mother":"Helen Lind","father":"Ove Lind"}},{"name":"Madeleine Dahl","parents":{"mother":"Elin Dahl","father":"Alexander Dahl"}},{"name":"Susanne Blomqvist","parents":{"mother":"Caroline Blomqvist","father":"Wilhelm Blomqvist"}},{"name":"Ulla Lundberg","parents":{"mother":"Olivia Lundberg","father":"William Lundberg"}},{"name":"Annika Nyberg","parents":{"mother":"Viktoria Nyberg","father":"Hans Nyberg"}},{"name":"Matilda Lundberg","parents":{"mother":"Cecilia Lundberg","father":"Johannes Lundberg"}},{"name":"Christian Ali","parents":{"mother":"Matilda Ali","father":"Nils Ali"}},{"name":"Emil Gustafsson","parents":{"mother":"Astrid Gustafsson","father":"Roger Gustafsson"}},{"name":"Kurt Lundgren","parents":{"mother":"Kerstin Lundgren","father":"Ove Lundgren"}},{"name":"Björn Lindberg","parents":{"mother":"Emelie Lindberg","father":"Per Lindberg"}},{"name":"Christer Nordin","parents":{"mother":"Inger Nordin","father":"Fredrik Nordin"}},{"name":"Johanna Nyström","parents":{"mother":"Britt Nyström","father":"Arvid Nyström"}},{"name":"Åke Olsson","parents":{"mother":"Madeleine Olsson","father":"Jakob Olsson"}},{"name":"Amanda Forsberg","parents":{"mother":"Klara Forsberg","father":"Nils Forsberg"}},{"name":"Susanne Håkansson","parents":{"mother":"Birgitta Håkansson","father":"Göran Håkansson"}},{"name":"Hans Löfgren","parents":{"mother":"Therese Löfgren","father":"Christoffer Löfgren"}},{"name":"Lisbeth Martinsson","parents":{"mother":"Carina Martinsson","father":"Viktor Martinsson"}},{"name":"Isak Holmgren","parents":{"mother":"Jenny Holmgren","father":"Jonas Holmgren"}},{"name":"Lovisa Nilsson","parents":{"mother":"Ellen Nilsson","father":"Per Nilsson"}},{"name":"Inger Ek","parents":{"mother":"Rut Ek","father":"Johannes Ek"}},{"name":"Bertil Arvidsson","parents":{"mother":"Rebecca Arvidsson","father":"Jakob Arvidsson"}},{"name":"Linnéa Jakobsson","parents":{"mother":"Ingrid Jakobsson","father":"Jonas Jakobsson"}},{"name":"Josef Olofsson","parents":{"mother":"Isabelle Olofsson","father":"Göran Olofsson"}},{"name":"Ingeborg Larsson","parents":{"mother":"Hanna Larsson","father":"Jonathan Larsson"}},{"name":"Mohamed Lund","parents":{"mother":"Olivia Lund","father":"Stig Lund"}},{"name":"Linus Nordin","parents":{"mother":"Inger Nordin","father":"Fredrik Nordin"}},{"name":"Viktoria Sandström","parents":{"mother":"Marianne Sandström","father":"Bo Sandström"}},{"name":"Lucas Lundberg","parents":{"mother":"Olivia Lundberg","father":"William Lundberg"}},{"name":"Pia Dahlberg","parents":{"mother":"Maja Dahlberg","father":"Lucas Dahlberg"}},{"name":"Bo Söderberg","parents":{"mother":"Emilia Söderberg","father":"Claes Söderberg"}},{"name":"Göran Bengtsson","parents":{"mother":"Irene Bengtsson","father":"Mats Bengtsson"}},{"name":"Ulf Mårtensson","parents":{"mother":"Kristin Mårtensson","father":"Georg Mårtensson"}},{"name":"Kerstin Hellström","parents":{"mother":"Camilla Hellström","father":"Robin Hellström"}},{"name":"Per Lund","parents":{"mother":"Eva Lund","father":"Arvid Lund"}},{"name":"Linnéa Blom","parents":{"mother":"Sandra Blom","father":"Robin Blom"}},{"name":"Siv Lund","parents":{"mother":"Ann Lund","father":"Olof Lund"}},{"name":"Elsa Fredriksson","parents":{"mother":"Linda Fredriksson","father":"Kjell Fredriksson"}},{"name":"Carina Strömberg","parents":{"mother":"Inger Strömberg","father":"Joakim Strömberg"}},{"name":"Amanda Nordin","parents":{"mother":"Julia Nordin","father":"Niklas Nordin"}},{"name":"Maj Lindström","parents":{"mother":"Malin Lindström","father":"Daniel Lindström"}},{"name":"Gustav Ali","parents":{"mother":"Pia Ali","father":"Lennart Ali"}},{"name":"Louise Strömberg","parents":{"mother":"Josefin Strömberg","father":"Christian Strömberg"}},{"name":"Åsa Nyström","parents":{"mother":"Caroline Nyström","father":"Johnny Nyström"}},{"name":"Gun Arvidsson","parents":{"mother":"Inga Arvidsson","father":"Isak Arvidsson"}},{"name":"Cecilia Hedlund","parents":{"mother":"Ida Hedlund","father":"Tommy Hedlund"}},{"name":"Johannes Arvidsson","parents":{"mother":"Ulla Arvidsson","father":"Olof Arvidsson"}},{"name":"Patrik Blomqvist","parents":{"mother":"Pia Blomqvist","father":"Johannes Blomqvist"}},{"name":"Oskar Isaksson","parents":{"mother":"Maj Isaksson","father":"Wilhelm Isaksson"}},{"name":"Albin Holmgren","parents":{"mother":"Marie Holmgren","father":"Daniel Holmgren"}},{"name":"Ida Eliasson","parents":{"mother":"Erika Eliasson","father":"John Eliasson"}},{"name":"Marianne Samuelsson","parents":{"mother":"Sofia Samuelsson","father":"Johannes Samuelsson"}},{"name":"Peter Ek","parents":{"mother":"Kristin Ek","father":"Christian Ek"}},{"name":"Hugo Strömberg","parents":{"mother":"Karin Strömberg","father":"Johannes Strömberg"}},{"name":"Siv Löfgren","parents":{"mother":"Therese Löfgren","father":"Christoffer Löfgren"}},{"name":"Tommy Norberg","parents":{"mother":"Jenny Norberg","father":"Hugo Norberg"}},{"name":"Charlotta Axelsson","parents":{"mother":"Charlotte Axelsson","father":"Filip Axelsson"}},{"name":"Maj Dahlberg","parents":{"mother":"Kerstin Dahlberg","father":"Joakim Dahlberg"}},{"name":"William Martinsson","parents":{"mother":"Anita Martinsson","father":"Robin Martinsson"}},{"name":"Dan Mattsson","parents":{"mother":"Louise Mattsson","father":"Mikael Mattsson"}},{"name":"Christer Holmgren","parents":{"mother":"Ulrika Holmgren","father":"Robin Holmgren"}},{"name":"Linus Bergqvist","parents":{"mother":"Viktoria Bergqvist","father":"Emanuel Bergqvist"}},{"name":"Torbjörn Holm","parents":{"mother":"Pia Holm","father":"Dan Holm"}},{"name":"Marcus Hellström","parents":{"mother":"Camilla Hellström","father":"Robin Hellström"}},{"name":"Kenneth Ali","parents":{"mother":"Viola Ali","father":"Kent Ali"}},{"name":"Frida Bergman","parents":{"mother":"Ebba Bergman","father":"Filip Bergman"}},{"name":"Karolina Lindberg","parents":{"mother":"Viktoria Lindberg","father":"Patrik Lindberg"}},{"name":"Sofia Johansson","parents":{"mother":"Ann Johansson","father":"Thomas Johansson"}},{"name":"Robin Berg","parents":{"mother":"Yvonne Berg","father":"Niklas Berg"}},{"name":"Niklas Hedlund","parents":{"mother":"Ulla Hedlund","father":"Torbjörn Hedlund"}},{"name":"Arne Arvidsson","parents":{"mother":"Camilla Arvidsson","father":"Roger Arvidsson"}},{"name":"Berit Hermansson","parents":{"mother":"Isabelle Hermansson","father":"Håkan Hermansson"}},{"name":"Torbjörn Hassan","parents":{"mother":"Isabelle Hassan","father":"Rickard Hassan"}},{"name":"Joakim Arvidsson","parents":{"mother":"Johanna Arvidsson","father":"Christer Arvidsson"}},{"name":"Carina Arvidsson","parents":{"mother":"Karolina Arvidsson","father":"Rune Arvidsson"}},{"name":"Georg Bergqvist","parents":{"mother":"Caroline Bergqvist","father":"Isak Bergqvist"}},{"name":"Britt Hellström","parents":{"mother":"Märta Hellström","father":"Anders Hellström"}},{"name":"Robert Magnusson","parents":{"mother":"Mona Magnusson","father":"Jonathan Magnusson"}},{"name":"Anton Mohamed","parents":{"mother":"Sara Mohamed","father":"Sebastian Mohamed"}},{"name":"Håkan Danielsson","parents":{"mother":"Anna Danielsson","father":"Roger Danielsson"}},{"name":"Malin Axelsson","parents":{"mother":"Charlotte Axelsson","father":"Filip Axelsson"}},{"name":"Alexander Pålsson","parents":{"mother":"Sandra Pålsson","father":"Christoffer Pålsson"}},{"name":"Lars Wallin","parents":{"mother":"Kristina Wallin","father":"Filip Wallin"}},{"name":"Magnus Sjöberg","parents":{"mother":"Frida Sjöberg","father":"Rickard Sjöberg"}},{"name":"Kurt Holmberg","parents":{"mother":"Ingegerd Holmberg","father":"Josef Holmberg"}},{"name":"Axel Holm","parents":{"mother":"Ellen Holm","father":"Kjell Holm"}},{"name":"Erika Sjöberg","parents":{"mother":"Helena Sjöberg","father":"Lars Sjöberg"}},{"name":"Oskar Sandström","parents":{"mother":"Olivia Sandström","father":"Emil Sandström"}},{"name":"Susanne Bengtsson","parents":{"mother":"Matilda Bengtsson","father":"Kjell Bengtsson"}},{"name":"Maja Hansen","parents":{"mother":"Klara Hansen","father":"Adam Hansen"}},{"name":"Sten Ek","parents":{"mother":"Frida Ek","father":"Viktor Ek"}},{"name":"Viola Axelsson","parents":{"mother":"Maria Axelsson","father":"Karl Axelsson"}},{"name":"Dan Ekström","parents":{"mother":"Lovisa Ekström","father":"Bertil Ekström"}},{"name":"Thomas Ekström","parents":{"mother":"Marie Ekström","father":"Göran Ekström"}},{"name":"Eva Håkansson","parents":{"mother":"Johanna Håkansson","father":"Karl Håkansson"}},{"name":"Georg Ahmed","parents":{"mother":"Anette Ahmed","father":"Fredrik Ahmed"}},{"name":"Maj Pålsson","parents":{"mother":"Sandra Pålsson","father":"Christoffer Pålsson"}},{"name":"Johnny Strömberg","parents":{"mother":"Madeleine Strömberg","father":"Anton Strömberg"}},{"name":"Rickard Holmgren","parents":{"mother":"Ulrika Holmgren","father":"Robin Holmgren"}},{"name":"Christer Strömberg","parents":{"mother":"Inger Strömberg","father":"Joakim Strömberg"}},{"name":"Åke Samuelsson","parents":{"mother":"Inger Samuelsson","father":"Gunnar Samuelsson"}},{"name":"Ingemar Sundberg","parents":{"mother":"Kristina Sundberg","father":"Anders Sundberg"}},{"name":"Jonas Åberg","parents":{"mother":"Birgit Åberg","father":"Joakim Åberg"}},{"name":"Olivia Ström","parents":{"mother":"Birgitta Ström","father":"Viktor Ström"}},{"name":"Marie Holmberg","parents":{"mother":"Ingegerd Holmberg","father":"Josef Holmberg"}},{"name":"Christoffer Nyström","parents":{"mother":"Caroline Nyström","father":"Johnny Nyström"}},{"name":"Yvonne Sandström","parents":{"mother":"Olivia Sandström","father":"Emil Sandström"}},{"name":"Carina Löfgren","parents":{"mother":"Camilla Löfgren","father":"Dan Löfgren"}},{"name":"Felicia Norberg","parents":{"mother":"Hanna Norberg","father":"Kjell Norberg"}},{"name":"Linnéa Nilsson","parents":{"mother":"Rebecca Nilsson","father":"Kurt Nilsson"}},{"name":"Jörgen Bergström","parents":{"mother":"Helena Bergström","father":"Lucas Bergström"}},{"name":"Daniel Larsson","parents":{"mother":"Hanna Larsson","father":"Jonathan Larsson"}},{"name":"Lisa Bergqvist","parents":{"mother":"Caroline Bergqvist","father":"Isak Bergqvist"}},{"name":"Charlotte Olsson","parents":{"mother":"Madeleine Olsson","father":"Jakob Olsson"}},{"name":"Niklas Hansen","parents":{"mother":"Klara Hansen","father":"Adam Hansen"}},{"name":"Anneli Bengtsson","parents":{"mother":"Matilda Bengtsson","father":"Kjell Bengtsson"}},{"name":"Bengt Arvidsson","parents":{"mother":"Ulla Arvidsson","father":"Olof Arvidsson"}},{"name":"Emanuel Martinsson","parents":{"mother":"Anneli Martinsson","father":"Nils Martinsson"}},{"name":"Emelie Lundström","parents":{"mother":"Felicia Lundström","father":"Mohamed Lundström"}},{"name":"Rebecca Bergqvist","parents":{"mother":"Therese Bergqvist","father":"Patrik Bergqvist"}},{"name":"Caroline Nyberg","parents":{"mother":"Frida Nyberg","father":"Mohamed Nyberg"}},{"name":"Maja Sandström","parents":{"mother":"Therese Sandström","father":"Dan Sandström"}},{"name":"Elisabeth Åberg","parents":{"mother":"Birgit Åberg","father":"Joakim Åberg"}},{"name":"Jonathan Dahlberg","parents":{"mother":"Caroline Dahlberg","father":"Peter Dahlberg"}},{"name":"Ulrika Jonsson","parents":{"mother":"Anneli Jonsson","father":"Jonathan Jonsson"}},{"name":"Johanna Lund","parents":{"mother":"Alice Lund","father":"Andreas Lund"}},{"name":"Erik Ali","parents":{"mother":"Matilda Ali","father":"Nils Ali"}},{"name":"Andreas Hermansson","parents":{"mother":"Camilla Hermansson","father":"Kenneth Hermansson"}},{"name":"Lena Norberg","parents":{"mother":"Jenny Norberg","father":"Hugo Norberg"}},{"name":"Charlotte Lundström","parents":{"mother":"Louise Lundström","father":"Joakim Lundström"}},{"name":"Roland Jakobsson","parents":{"mother":"Ingrid Jakobsson","father":"Jonas Jakobsson"}},{"name":"Sandra Lundström","parents":{"mother":"Louise Lundström","father":"Joakim Lundström"}},{"name":"Rut Lindström","parents":{"mother":"Malin Lindström","father":"Daniel Lindström"}},{"name":"Josef Lund","parents":{"mother":"Eva Lund","father":"Arvid Lund"}},{"name":"Elin Arvidsson","parents":{"mother":"Johanna Arvidsson","father":"Christer Arvidsson"}},{"name":"Rut Martinsson","parents":{"mother":"Carina Martinsson","father":"Viktor Martinsson"}},{"name":"Joakim Ström","parents":{"mother":"Birgitta Ström","father":"Viktor Ström"}},{"name":"Siv Holmgren","parents":{"mother":"Jenny Holmgren","father":"Jonas Holmgren"}},{"name":"Anton Ekström","parents":{"mother":"Rut Ekström","father":"Alexander Ekström"}},{"name":"Arne Bergqvist","parents":{"mother":"Mona Bergqvist","father":"Marcus Bergqvist"}},{"name":"Jörgen Sandström","parents":{"mother":"Therese Sandström","father":"Dan Sandström"}},{"name":"Jörgen Eliasson","parents":{"mother":"Inga Eliasson","father":"Ulf Eliasson"}},{"name":"Oskar Ström","parents":{"mother":"Inga Ström","father":"Rickard Ström"}},{"name":"Wilhelm Gunnarsson","parents":{"mother":"Anneli Gunnarsson","father":"Kenneth Gunnarsson"}},{"name":"Ingemar Bergman","parents":{"mother":"Ebba Bergman","father":"Filip Bergman"}},{"name":"Ulf Håkansson","parents":{"mother":"Therese Håkansson","father":"Per Håkansson"}},{"name":"Alf Lindberg","parents":{"mother":"Cecilia Lindberg","father":"Rickard Lindberg"}},{"name":"Jan Lundström","parents":{"mother":"Felicia Lundström","father":"Mohamed Lundström"}},{"name":"Gunilla Pålsson","parents":{"mother":"Ulla Pålsson","father":"Stig Pålsson"}},{"name":"Lisa Henriksson","parents":{"mother":"Inga Henriksson","father":"Rune Henriksson"}},{"name":"Jessica Hedlund","parents":{"mother":"Ulla Hedlund","father":"Torbjörn Hedlund"}},{"name":"Joakim Karlsson","parents":{"mother":"Olivia Karlsson","father":"Georg Karlsson"}},{"name":"Sara Ström","parents":{"mother":"Astrid Ström","father":"Henrik Ström"}},{"name":"Ann Gunnarsson","parents":{"mother":"Maja Gunnarsson","father":"Ingemar Gunnarsson"}},{"name":"Matilda Norberg","parents":{"mother":"Elin Norberg","father":"Elias Norberg"}},{"name":"Siv Holm","parents":{"mother":"Pia Holm","father":"Dan Holm"}},{"name":"Ebba Mattsson","parents":{"mother":"Britt Mattsson","father":"Oliver Mattsson"}},{"name":"Anton Wallin","parents":{"mother":"Emilia Wallin","father":"Anders Wallin"}},{"name":"Elin Persson","parents":{"mother":"Anette Persson","father":"Mats Persson"}},{"name":"Sofie Holm","parents":{"mother":"Ellen Holm","father":"Kjell Holm"}},{"name":"Adam Henriksson","parents":{"mother":"Inga Henriksson","father":"Rune Henriksson"}},{"name":"Rickard Nyberg","parents":{"mother":"Frida Nyberg","father":"Mohamed Nyberg"}},{"name":"Anette Norberg","parents":{"mother":"Elin Norberg","father":"Elias Norberg"}},{"name":"Rune Åberg","parents":{"mother":"Karin Åberg","father":"Torbjörn Åberg"}},{"name":"Linda Abrahamsson","parents":{"mother":"Viola Abrahamsson","father":"Wilhelm Abrahamsson"}},{"name":"Håkan Arvidsson","parents":{"mother":"Karolina Arvidsson","father":"Rune Arvidsson"}},{"name":"Hans Hermansson","parents":{"mother":"Isabelle Hermansson","father":"Håkan Hermansson"}},{"name":"Gustav Ek","parents":{"mother":"Frida Ek","father":"Viktor Ek"}},{"name":"Jan Bergqvist","parents":{"mother":"Susanne Bergqvist","father":"Fredrik Bergqvist"}},{"name":"Eva Holmgren","parents":{"mother":"Sofia Holmgren","father":"Stefan Holmgren"}},{"name":"Per Karlsson","parents":{"mother":"Eva Karlsson","father":"Kenneth Karlsson"}},{"name":"Olof Håkansson","parents":{"mother":"Birgitta Håkansson","father":"Göran Håkansson"}},{"name":"Göran Hermansson","parents":{"mother":"Anna Hermansson","father":"David Hermansson"}},{"name":"Kristina Håkansson","parents":{"mother":"Margareta Håkansson","father":"Stig Håkansson"}},{"name":"Anton Lindström","parents":{"mother":"Linda Lindström","father":"Magnus Lindström"}},{"name":"Erika Ahmed","parents":{"mother":"Susanne Ahmed","father":"Stefan Ahmed"}},{"name":"Birgitta Bergström","parents":{"mother":"Helena Bergström","father":"Lucas Bergström"}},{"name":"Hugo Svensson","parents":{"mother":"Gun Svensson","father":"Linus Svensson"}},{"name":"Matilda Håkansson","parents":{"mother":"Camilla Håkansson","father":"Thomas Håkansson"}},{"name":"Ann-Marie Larsson","parents":{"mother":"Siv Larsson","father":"Ali Larsson"}},{"name":"Sebastian Holmgren","parents":{"mother":"Marie Holmgren","father":"Daniel Holmgren"}},{"name":"Lena Samuelsson","parents":{"mother":"Agneta Samuelsson","father":"Arvid Samuelsson"}},{"name":"Mats Holmgren","parents":{"mother":"Agnes Holmgren","father":"Ingvar Holmgren"}},{"name":"Ann-Marie Holmgren","parents":{"mother":"Gunilla Holmgren","father":"Johannes Holmgren"}},{"name":"Lars Strömberg","parents":{"mother":"Josefin Strömberg","father":"Christian Strömberg"}},{"name":"Helena Mårtensson","parents":{"mother":"Louise Mårtensson","father":"Alexander Mårtensson"}},{"name":"Elsa Holmgren","parents":{"mother":"Gunilla Holmgren","father":"Johannes Holmgren"}},{"name":"Rickard Henriksson","parents":{"mother":"Ingeborg Henriksson","father":"Mikael Henriksson"}},{"name":"Nils Andersson","parents":{"mother":"Astrid Andersson","father":"Josef Andersson"}},{"name":"Hugo Mårtensson","parents":{"mother":"Kristin Mårtensson","father":"Georg Mårtensson"}},{"name":"Berit Martinsson","parents":{"mother":"Anneli Martinsson","father":"Nils Martinsson"}},{"name":"Björn Gustafsson","parents":{"mother":"Malin Gustafsson","father":"Erik Gustafsson"}},{"name":"Ellen Viklund","parents":{"mother":"Camilla Viklund","father":"Albin Viklund"}},{"name":"Ali Andersson","parents":{"mother":"Astrid Andersson","father":"Josef Andersson"}},{"name":"Lena Holmgren","parents":{"mother":"Agnes Holmgren","father":"Ingvar Holmgren"}},{"name":"Elsa Jonsson","parents":{"mother":"Anneli Jonsson","father":"Jonathan Jonsson"}},{"name":"Ingvar Berg","parents":{"mother":"Britt Berg","father":"Isak Berg"}},{"name":"Torbjörn Jonsson","parents":{"mother":"Therese Jonsson","father":"Olof Jonsson"}},{"name":"Margareta Bergström","parents":{"mother":"Märta Bergström","father":"Tommy Bergström"}},{"name":"Katarina Viklund","parents":{"mother":"Camilla Viklund","father":"Albin Viklund"}},{"name":"Viola Lindberg","parents":{"mother":"Gunilla Lindberg","father":"Isak Lindberg"}},{"name":"Ali Eriksson","parents":{"mother":"Berit Eriksson","father":"Niklas Eriksson"}},{"name":"Filip Nilsson","parents":{"mother":"Ellen Nilsson","father":"Per Nilsson"}},{"name":"Ulf Axelsson","parents":{"mother":"Anita Axelsson","father":"Isak Axelsson"}},{"name":"Yvonne Åberg","parents":{"mother":"Karin Åberg","father":"Torbjörn Åberg"}},{"name":"Lucas Sandström","parents":{"mother":"Erika Sandström","father":"Rickard Sandström"}},{"name":"Caroline Söderberg","parents":{"mother":"Ingegerd Söderberg","father":"Johnny Söderberg"}},{"name":"Monica Ström","parents":{"mother":"Sofia Ström","father":"Bo Ström"}},{"name":"Tobias Svensson","parents":{"mother":"Gun Svensson","father":"Linus Svensson"}},{"name":"Emilia Fransson","parents":{"mother":"Agnes Fransson","father":"John Fransson"}},{"name":"Dan Engström","parents":{"mother":"Elisabeth Engström","father":"Åke Engström"}},{"name":"Magnus Mohamed","parents":{"mother":"Sara Mohamed","father":"Sebastian Mohamed"}},{"name":"Karl Nyberg","parents":{"mother":"Viktoria Nyberg","father":"Hans Nyberg"}},{"name":"Magnus Håkansson","parents":{"mother":"Camilla Håkansson","father":"Thomas Håkansson"}},{"name":"Helena Bergqvist","parents":{"mother":"Rut Bergqvist","father":"Jakob Bergqvist"}},{"name":"Ann-Marie Arvidsson","parents":{"mother":"Camilla Arvidsson","father":"Roger Arvidsson"}},{"name":"Susanne Arvidsson","parents":{"mother":"Inger Arvidsson","father":"Nils Arvidsson"}},{"name":"Karin Arvidsson","parents":{"mother":"Inga Arvidsson","father":"Isak Arvidsson"}},{"name":"Nils Berglund","parents":{"mother":"Ingegerd Berglund","father":"Kjell Berglund"}},{"name":"Elsa Karlsson","parents":{"mother":"Eva Karlsson","father":"Kenneth Karlsson"}},{"name":"Hugo Nyberg","parents":{"mother":"Kristina Nyberg","father":"Stig Nyberg"}},{"name":"Karl Jonsson","parents":{"mother":"Therese Jonsson","father":"Olof Jonsson"}},{"name":"Ove Wallin","parents":{"mother":"Kristina Wallin","father":"Filip Wallin"}},{"name":"Annika Lindström","parents":{"mother":"Elisabeth Lindström","father":"Mattias Lindström"}},{"name":"Lena Hermansson","parents":{"mother":"Anna Hermansson","father":"David Hermansson"}},{"name":"Agneta Lindholm","parents":{"mother":"Ulrika Lindholm","father":"Hans Lindholm"}},{"name":"Rebecca Bergström","parents":{"mother":"Irene Bergström","father":"Kurt Bergström"}},{"name":"Kjell Ström","parents":{"mother":"Inga Ström","father":"Rickard Ström"}},{"name":"Elias Lind","parents":{"mother":"Ingeborg Lind","father":"Adam Lind"}},{"name":"Emanuel Blomqvist","parents":{"mother":"Anette Blomqvist","father":"Jakob Blomqvist"}},{"name":"Linnéa Björklund","parents":{"mother":"Rut Björklund","father":"Mikael Björklund"}},{"name":"Olivia Svensson","parents":{"mother":"Klara Svensson","father":"Emanuel Svensson"}},{"name":"Rickard Bergqvist","parents":{"mother":"Mona Bergqvist","father":"Marcus Bergqvist"}},{"name":"Thomas Pålsson","parents":{"mother":"Ingrid Pålsson","father":"Jonathan Pålsson"}},{"name":"Kerstin Sjögren","parents":{"mother":"Susanne Sjögren","father":"Viktor Sjögren"}},{"name":"Robin Mårtensson","parents":{"mother":"Gunilla Mårtensson","father":"Niklas Mårtensson"}},{"name":"Mona Arvidsson","parents":{"mother":"Inger Arvidsson","father":"Nils Arvidsson"}},{"name":"Viktoria Björklund","parents":{"mother":"Marianne Björklund","father":"Jan Björklund"}},{"name":"Olivia Nilsson","parents":{"mother":"Rebecca Nilsson","father":"Kurt Nilsson"}},{"name":"Monica Dahlberg","parents":{"mother":"Ingrid Dahlberg","father":"Arne Dahlberg"}},{"name":"Inger Lindholm","parents":{"mother":"Maja Lindholm","father":"Alexander Lindholm"}},{"name":"Arvid Lind","parents":{"mother":"Helen Lind","father":"Ove Lind"}},{"name":"Erik Björklund","parents":{"mother":"Ulrika Björklund","father":"Thomas Björklund"}},{"name":"Elin Berg","parents":{"mother":"Ulrika Berg","father":"Hugo Berg"}},{"name":"Emil Bergqvist","parents":{"mother":"Rut Bergqvist","father":"Jakob Bergqvist"}}]'

data = json.loads(children)

def cls():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    while True:
        cls()
        print(".: Child Locator 2.0.0 :.")
        print("-------------------------")
        father = input("Father   > ").capitalize()
        mother = input("Mother   > ").capitalize()
        surname = input("Surname  > ").capitalize()
        print("-------------------------")
        count = 0
        for child in filter(lambda x: x["parents"]["father"] == father + " " + surname and x["parents"]["mother"] == mother + " " + surname, data):
            print(" * " + child["name"])
            count += 1
        if count == 0:
            print(f"{'No children found..':^25}")
            print(f"{':(':^25}")
        print("-------------------------")
        input(f"""{'Press enter to':^25}
{'search again...':^25}""")


if __name__ == "__main__": main()
