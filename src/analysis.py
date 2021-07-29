from matplotlib import pyplot as plt
import operator


class PieBarChart:
    """This class plot the bar chart and pie chart"""
    def __init__(self, words, frequency):
        self.words = words
        self.frequency = frequency

    def bar_chart(self):
        """This function is responsible for plotting the Bar Chart"""
        plt.xlabel('words')
        plt.ylabel('frequency of words')
        plt.title(f'Words in python.org')
        plt.xticks(fontsize=10)
        plt.bar(self.words, self.frequency, width=0.8)
        return plt.show()

    def pie_chart(self):
        """This function is responsible for plotting the Pie Chart"""
        fig = plt.figure()
        ax = fig.add_axes([0, 0, 1, 1])
        ax.set_title('most common words')
        ax.axis('equal')
        ax.set_title('most common words')
        ax.pie(self.frequency, labels=self.words, autopct='%1.2f%%')
        return plt.show()

    def top_word(self, dic):
        """This function is responsible for returning the most common 10 words """
        highest_word = max(dic.items(), key=operator.itemgetter(1))[0]
        print(f'The top word is: {highest_word}')
        return highest_word


