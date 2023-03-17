class Boxtype:
    id: int
    l: int; w: int; h: int
    rotx: bool; roty: bool; rotz: bool
    weight: int

    def __init__(self, id, l, w, h, rotx=True, roty=True, rotz=True, weight=1):
        self.id = id
        self.l = l; self.w = w; self.h = h
        self.rotx, self.roty, self.rotz = rotx, roty, rotz
        self.weight = weight

    def volume(self):
        return self.l*self.w*self.h

# Items are pairs (Boxtype, quantity)
class Itemdict(dict):
  def __iadd__(self, other):
      for key in other:
          if key in self:
              self[key] += other[key]
          else:
              self[key] = other[key]
      return self

  def __isub__(self, other):
      for key in other:
          if key in self:
              self[key] -= other[key]
          else:
              self[key] = -other[key]
      return self

#An Aabb is cuboid+location
#Useful for representing free space cuboids and placed blocks
class Aabb:
    xmin: int; xmax: int
    ymin: int; ymax: int
    zmin: int; zmax: int
    l: int; w: int; h: int
    manhattan: int
    volume: int

    def __init__(self, xmin, xmax, ymin, ymax, zmin, zmax):
        self.xmin = xmin; self.xmax = xmax
        self.ymin = ymin; self.ymax = ymax
        self.zmin = zmin; self.zmax = zmax
        self.volume = (xmax-xmin)*(ymax-ymin)*(zmax-zmin)
        self.l = xmax-xmin; self.w = ymax-ymin; self.h = zmax-zmin
        self.manhattan = self.xmin + self.ymin + self.zmin
    
    # returns true if aabb is inside self
    def strict_intersects(self, aabb):
        return self.xmin < aabb.xmax and self.xmax > aabb.xmin and self.ymin < aabb.ymax and self.ymax > aabb.ymin and self.zmin < aabb.zmax and self.zmax > aabb.zmin
    
    # returns true if aabb intersects self
    def intersects(self, aabb):
        return self.xmin <= aabb.xmax and self.xmax >= aabb.xmin and self.ymin <= aabb.ymax and self.ymax >= aabb.ymin and self.zmin <= aabb.zmax and self.zmax >= aabb.zmin
    
    # returns a list of aabbs that are the result of substracting aabb from self    
    def subtract(self, aabb):
        sub = list()
        if aabb.xmax < self.xmax:
            sub.append(Aabb(aabb.xmax, self.xmax, self.ymin, self.ymax, self.zmin, self.zmax))
        if aabb.ymax < self.ymax:
            sub.append(Aabb(self.xmin, self.xmax, aabb.ymax, self.ymax, self.zmin, self.zmax))
        if aabb.zmax < self.zmax:
            sub.append(Aabb(self.xmin, self.xmax, self.ymin, self.ymax, aabb.zmax, self.zmax))
        if aabb.xmin > self.xmin:
            sub.append(Aabb(self.xmin, aabb.xmin, self.ymin, self.ymax, self.zmin, self.zmax))
        if aabb.ymin > self.ymin:
            sub.append(Aabb(self.xmin, self.xmax, self.ymin, aabb.ymin, self.zmin, self.zmax))
        if aabb.zmin > self.zmin:
            sub.append(Aabb(self.xmin, self.xmax, self.ymin, self.ymax, self.zmin, aabb.zmin))
        return sub
    
    def can_contain(self, aabb):
        return self.l >= aabb.l and self.w >= aabb.w and self.h >= aabb.h
    
    # aabb is contained in self
    def __ge__(self, aabb):
        return self.xmin <= aabb.xmin and self.xmax >= aabb.xmax and self.ymin <= aabb.ymin and self.ymax >= aabb.ymax and self.zmin <= aabb.zmin and self.zmax >= aabb.zmax
    
    def __str__(self):
        return "Aabb: xmin: " + str(self.xmin) + " xmax: " + str(self.xmax) + " ymin: " + str(self.ymin) + " ymax: " + str(self.ymax) + " zmin: " + str(self.zmin) + " zmax: " + str(self.zmax)

class Boxtype:
    id: int
    l: int; w: int; h: int
    rotx: bool; roty: bool; rotz: bool
    weight: int

    def __init__(self, id, l, w, h, rotx=True, roty=True, rotz=True, weight=1):
        self.id = id
        self.l = l; self.w = w; self.h = h
        self.rotx, self.roty, self.rotz = rotx, roty, rotz
        self.weight = weight

    def volume(self):
        return self.l*self.w*self.h

# Items are pairs (Boxtype, quantity)
class Itemdict(dict):
  def __iadd__(self, other):
      for key in other:
          if key in self:
              self[key] += other[key]
          else:
              self[key] = other[key]
      return self

  def __isub__(self, other):
      for key in other:
          if key in self:
              self[key] -= other[key]
          else:
              self[key] = -other[key]
      return self

#An Aabb is cuboid+location
#Useful for representing free space cuboids and placed blocks
class Aabb:
    xmin: int; xmax: int
    ymin: int; ymax: int
    zmin: int; zmax: int
    l: int; w: int; h: int
    manhattan: int
    volume: int

    def __init__(self, xmin, xmax, ymin, ymax, zmin, zmax):
        self.xmin = xmin; self.xmax = xmax
        self.ymin = ymin; self.ymax = ymax
        self.zmin = zmin; self.zmax = zmax
        self.volume = (xmax-xmin)*(ymax-ymin)*(zmax-zmin)
        self.l = xmax-xmin; self.w = ymax-ymin; self.h = zmax-zmin
        self.manhattan = self.xmin + self.ymin + self.zmin
    
    # returns true if aabb is inside self
    def strict_intersects(self, aabb):
        return self.xmin < aabb.xmax and self.xmax > aabb.xmin and self.ymin < aabb.ymax and self.ymax > aabb.ymin and self.zmin < aabb.zmax and self.zmax > aabb.zmin
    
    # returns true if aabb intersects self
    def intersects(self, aabb):
        return self.xmin <= aabb.xmax and self.xmax >= aabb.xmin and self.ymin <= aabb.ymax and self.ymax >= aabb.ymin and self.zmin <= aabb.zmax and self.zmax >= aabb.zmin
    
    # returns a list of aabbs that are the result of substracting aabb from self    
    def subtract(self, aabb):
        sub = list()
        if aabb.xmax < self.xmax:
            sub.append(Aabb(aabb.xmax, self.xmax, self.ymin, self.ymax, self.zmin, self.zmax))
        if aabb.ymax < self.ymax:
            sub.append(Aabb(self.xmin, self.xmax, aabb.ymax, self.ymax, self.zmin, self.zmax))
        if aabb.zmax < self.zmax:
            sub.append(Aabb(self.xmin, self.xmax, self.ymin, self.ymax, aabb.zmax, self.zmax))
        if aabb.xmin > self.xmin:
            sub.append(Aabb(self.xmin, aabb.xmin, self.ymin, self.ymax, self.zmin, self.zmax))
        if aabb.ymin > self.ymin:
            sub.append(Aabb(self.xmin, self.xmax, self.ymin, aabb.ymin, self.zmin, self.zmax))
        if aabb.zmin > self.zmin:
            sub.append(Aabb(self.xmin, self.xmax, self.ymin, self.ymax, self.zmin, aabb.zmin))
        return sub
    
    def can_contain(self, aabb):
        return self.l >= aabb.l and self.w >= aabb.w and self.h >= aabb.h
    
    # aabb is contained in self
    def __ge__(self, aabb):
        return self.xmin <= aabb.xmin and self.xmax >= aabb.xmax and self.ymin <= aabb.ymin and self.ymax >= aabb.ymax and self.zmin <= aabb.zmin and self.zmax >= aabb.zmax
    
    def __str__(self):
        return "Aabb: xmin: " + str(self.xmin) + " xmax: " + str(self.xmax) + " ymin: " + str(self.ymin) + " ymax: " + str(self.ymax) + " zmin: " + str(self.zmin) + " zmax: " + str(self.zmax)

#FreeSpaace represent the free space inside a block
#Consists of a list of free space aabbs (spaces)
class FreeSpace:
    spaces : list() # list of aabbs
    def __init__(self, aabb=None):
        self.spaces = list()
        if aabb is not None:
          self.spaces.append(aabb)

    def remove_nonmaximal_spaces(self, aabbs):
      #sort aabbs by volume
      aabbs.sort(key=lambda aabb: aabb.volume, reverse=True)

      for i in range(len(aabbs)):
        if i>=len(aabbs): break
        for j in range(i+1, len(aabbs)):   
          if j>=len(aabbs): break
          if aabbs[i] >= aabbs[j]:
              aabbs.remove(aabbs[j])
              j -= 1
          
    def crop(self, aabb):
        new_spaces = list()
        to_remove = list()
        for space in self.spaces:
            if space.intersects(aabb):                
                if space.strict_intersects(aabb):
                    sub = space.subtract(aabb)
                    for s in sub: new_spaces.append(s)
                else:
                    new_spaces.append(space)
                
                to_remove.append(space)

        for sp in to_remove: self.spaces.remove(sp)

        self.remove_nonmaximal_spaces(new_spaces)

        self.spaces.extend(new_spaces)

    #compute the free space closer to the origin (manhattan distance)
    def closest_space(self):
        min = 1000000; cspace=None
        for space in self.spaces:
            if space.manhattan < min: 
              min = space.manhattan
              cspace = space
        if cspace == None: return None, None
        else: return (cspace.xmin, cspace.ymin, cspace.zmin), cspace


    #remove all spaces that cannot be filled by a boxtype
    def filter(self, items):
        to_remove = list()
        for space in self.spaces:
            remove = True
            for item in items:
                if items[item]>0 and space.l >= item.l and space.w >= item.w and space.h >= item.h:
                    remove = False
                    break
            if remove==True: to_remove.append(space)

        for sp in to_remove: self.spaces.remove(sp)

    def __str__(self):
        _str = ""
        for space in self.spaces:
          _str+= str(space) +"\n"
        return _str

#A block is compund by a set of items(boxtype+quantity)
#The container is a block
class Block:
    l: int; w: int; h: int
    occupied_volume: int
    weight: int
    items: Itemdict() # Boxtype: int
    volume: int
    free_space: FreeSpace() # list of free spaces

    def __init__(self, boxtype=None, rot=True, l=0, w=0, h=0):
        if boxtype is not None:
          if rot[0]=='w': self.l = boxtype.w
          elif rot[1]=='w': self.w = boxtype.w
          elif rot[2]=='w': self.h = boxtype.w

          if rot[0]=='l': self.l = boxtype.l
          elif rot[1]=='l': self.w = boxtype.l
          elif rot[2]=='l': self.h = boxtype.l        

          if rot[0]=='h': self.l = boxtype.h
          elif rot[1]=='h': self.w = boxtype.h
          elif rot[2]=='h': self.h = boxtype.h
          
          self.weight = boxtype.weight
          self.occupied_volume = boxtype.volume()
          self.volume = boxtype.volume()
          self.items = Itemdict()
          self.items[boxtype] = 1
          self.free_spaces = FreeSpace() # empty list of free spaces

        else: 
          self.l = l; self.w = w; self.h = h
          self.occupied_volume = 0
          self.weight = 0
          self.items = Itemdict()
          self.volume = l*w*h
          self.free_space = FreeSpace(Aabb(0, self.l, 0, self.w, 0, self.h)) # all is free space

    def add_block(self, block, location):
        x, y, z = location
        self.occupied_volume += block.occupied_volume
        self.weight += block.weight
        self.items += block.items
        self.free_space.crop(Aabb(x, x+block.l, y, y+block.w, z, z+block.h)) # remove the space occupied by the block


    #x:w, y:l, z:h
    def join(self, block, dim, min_fr=0.98):
        if dim=='x':
            l = self.l + block.l; w = max(self.w, block.w); h = max(self.h, block.h); volume = w*l*h
            if (self.occupied_volume + block.occupied_volume)/volume < min_fr: return False
            self.weight += block.weight
            self.occupied_volume += block.occupied_volume
            self.volume = volume
            self.items += block.items
        elif dim=='y':
            l = max(self.l, block.l); w = self.w + block.w; h = max(self.h, block.h); volume = w*l*h
            if (self.occupied_volume + block.occupied_volume)/volume < min_fr: return False
            self.weight += block.weight
            self.occupied_volume += block.occupied_volume
            self.volume = volume
            self.items += block.items
        elif dim=='z':
            l = max(self.l, block.l); w = max(self.w, block.w); h = self.h + block.h; volume = w*l*h
            if (self.occupied_volume + block.occupied_volume)/volume < min_fr: return False
            self.weight += block.weight
            self.occupied_volume += block.occupied_volume
            self.volume = volume
            self.items += block.items
        self.l = l; self.w = w; self.h = h

        return True

    def occupied_volume_ratio(self):
        return self.occupied_volume/self.volume
      
    def __str__(self):
        return "Block: l: " + str(self.l) + " w: " + str(self.w) + " h: " + str(self.h) + " weight: " + str(self.weight) + " volume: " + str(self.volume) + " occupied_volume: " + str(self.occupied_volume) + " items: " + str(self.items) + " ratio:" + str(self.occupied_volume_ratio())

class BlockList(list):
    def __init__(self, items, type, *args):
        super().__init__(*args)
        if(type=="simple_blocks"):
            self.generate_simple_blocks(items)

    def generate_simple_blocks(self,items):
        for item in items:
            self.append(Block(item,"lwh"))
            self.append(Block(item,"whl"))
            self.append(Block(item,"hwl"))
            self.append(Block(item,"hlw"))
            self.append(Block(item,"lhw"))
            self.append(Block(item,"wlh"))

    def largest(blocks, maxL, maxW, maxH):
        largest = None
        for block in blocks:
            if block.w <= maxW and block.l <= maxL and block.h <= maxH:
                if largest is None or block.volume > largest.volume:
                    largest = block
        return largest

    #remove blocks that cannot be constructed with the given items(boxtype->number)
    def remove_unconstructable(blocks, items):
        #cannot remove while iterating
        to_remove = list()
        for block in blocks:
            for item in block.items:
                if items[item] < block.items[item]:
                    to_remove.append(block)
                    break
        for block in to_remove:
            blocks.remove(block)

    def __str__(self):
        _str = ""
        for block in self:
            _str+= str(block) + "\n"



