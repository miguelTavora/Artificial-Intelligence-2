class CityData:

    @property
    def data(self):
        data_content = {
            'Dhaka' : [  0, 290, 250,  230,  190,  334, 365,   40],
            'Syhlet' : [290,   0, 337,  453,  396,  560, 581,  244],
            'Chittagonj' : [250, 337,   0,  495,  396,  540, 120,  240],
            'Rajshahi' : [230, 453, 495,    0,  360,  150, 595,  242],
            'Jossore' : [190, 396, 396,  360,    0,  356, 496,  253],
            'Dinajpur' : [334, 560, 540,  150,  356,    0, 674,  275],
            'Coxsbazar' : [365, 581, 120,  595,  496,  674,   0,  397],
            'Narsingdi' : [40,  244, 240,  242,  253,  275, 397,    0]
        }
        return data_content

    @property
    def coordinates(self):
        coord = {
            'Dhaka' : [23.7806146, 90.3368807],
            'Syhlet' : [24.8997579, 91.8197823],
            'Chittagonj' : [22.3259135, 91.7374667],
            'Rajshahi' : [24.3801485, 88.5648163],
            'Jossore' : [23.0841038, 88.8762695],
            'Dinajpur' : [25.6237783, 88.6055513],
            'Coxsbazar' : [21.4508931, 91.9617024],
            'Narsingdi' : [23.9194804,90.7069445]
        }
        return coord