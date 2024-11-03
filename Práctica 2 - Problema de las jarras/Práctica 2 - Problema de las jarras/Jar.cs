using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Práctica_2___Problema_de_las_jarras
{
    public class Jar
    {
        private int capacity;
        private int currentVolume;

        public Jar(int capacity)
        {
            this.capacity = capacity;
            this.currentVolume = 0;
        }

        public Jar(Jar other)
        {
            this.capacity = other.capacity;
            this.currentVolume = other.currentVolume;
        }

        public int getCapacity()
        {
            return this.capacity;
        }

        public int getCurrentVolume()
        {
            return this.currentVolume;
        }

        public void empty()
        {
            this.currentVolume = 0;
        }

        public void fill()
        {
            this.currentVolume = capacity;
        }

        public void fill(Jar other)
        {
            var otherVolume = other.getCurrentVolume();

            if(otherVolume + this.currentVolume >= this.capacity)
            {
                otherVolume -= this.capacity - this.currentVolume;
                this.currentVolume = this.capacity;
                other.fill(otherVolume);
            }
            else
            {
                this.currentVolume += otherVolume;
                other.empty();
            }
        }

        protected void fill(int volume)
        {
            this.currentVolume = volume;
        }

    }
}
