def setup(self):
    """Set up the game here. Call this function to restart the game."""

    # Set up the Cameras
    self.camera = arcade.Camera(self.width, self.height)
    self.gui_camera = arcade.Camera(self.width, self.height)

    # Map name
    map_name = ":resources:tiled_maps/map_with_ladders.json"

    # Layer Specific Options for the Tilemap
    layer_options = {
        LAYER_NAME_PLATFORMS: {
            "use_spatial_hash": True,
        },
        LAYER_NAME_MOVING_PLATFORMS: {
            "use_spatial_hash": False,
        },
        LAYER_NAME_LADDERS: {
            "use_spatial_hash": True,
        },
        LAYER_NAME_COINS: {
            "use_spatial_hash": True,
        },
    }

    # Load in TileMap
    self.tile_map = arcade.load_tilemap(map_name, TILE_SCALING, layer_options)

    # Initiate New Scene with our TileMap, this will automatically add all layers
    # from the map as SpriteLists in the scene in the proper order.
    self.scene = arcade.Scene.from_tilemap(self.tile_map)

    # Keep track of the score
    self.score = 0

    # Set up the player, specifically placing it at these coordinates.
    image_source = ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png"
    self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
    self.player_sprite.center_x = PLAYER_START_X
    self.player_sprite.center_y = PLAYER_START_Y
    self.scene.add_sprite("Player", self.player_sprite)

    # Calculate the right edge of the my_map in pixels
    self.end_of_map = self.tile_map.width * GRID_PIXEL_SIZE

    # --- Other stuff
    # Set the background color
    if self.tile_map.background_color:
        arcade.set_background_color(self.tile_map.background_color)

    # Create the 'physics engine'
    self.physics_engine = arcade.PhysicsEnginePlatformer(
        self.player_sprite,
        platforms=self.scene[LAYER_NAME_MOVING_PLATFORMS],
        gravity_constant=GRAVITY,
        ladders=self.scene[LAYER_NAME_LADDERS],
        walls=self.scene[LAYER_NAME_PLATFORMS]
    )