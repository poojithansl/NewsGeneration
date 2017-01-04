from utils import InputText
import tensorflow as tf

from utils import InputText
class Model():
    def __init__(self):
        cell=tf.nn.rnn_cell.BasicLSTMCell
        self.cell=tf.rnn_cell.MultiRNNCell([])
        self.input_data = tf.placeholder(tf.int32, [args.batch_size, args.seq_length])
        self.targets = tf.placeholder(tf.int32, [args.batch_size, args.seq_length])
        self._initial_state = cell.zero_state(batch_size, data_type())





def train():
    data=InputText()
