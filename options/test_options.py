from .base_options import BaseOptions


class TestOptions(BaseOptions):
    """This class includes test options.

    It also includes shared options defined in BaseOptions.
    """

    def initialize(self, parser):
        parser = BaseOptions.initialize(self, parser)  # define shared options
        parser.add_argument('--results_dir', type=str, default='./results/', help='saves results here.')
        parser.add_argument('--phase', type=str, default='test', help='train, val, test, etc')
        # Dropout and Batchnorm has different behavioir during training and test.
        parser.add_argument('--eval', action='store_true', help='use eval mode during test time.')
        parser.add_argument('--num_test', type=int, default=3000, help='how many test images to run')
        parser.add_argument(
            '--style_weights', type=str, default=None,
            help='Comma separated weights for multiple style images, e.g. "0.6,0.4"')
        parser.add_argument('--many_content_path', type=str, default='',
                            help='Path to the content image for multi-style transfer')
        parser.add_argument('--many_style_transfer', type=str, default='False',
                            help='Path to the content image for multi-style transfer')
        parser.add_argument('--many_style_path', type=str, default='',
                            help='Comma separated paths to style images for multi-style transfer')

        # rewrite devalue values
        parser.set_defaults(model='test')
        # To avoid cropping, the load_size should be the same as crop_size
        parser.set_defaults(load_size=parser.get_default('crop_size'))

        self.isTrain = False
        return parser
